"""Sync with a radiusdesk database."""

import time

from mysql.connector import connect
from django.conf import settings
from django.utils.timezone import make_aware

from monitoring.models import Cloud, Mesh, Node, NodeStation, NodeLoad, UptimeMetric


GET_CLOUDS_QUERY = """
SELECT name, description, lat, lng, created
FROM clouds;"""
GET_MESHES_QUERY = """
SELECT m.name, m.ssid, c.name, m.created
FROM meshes m
JOIN clouds c
ON m.cloud_id = c.id;
"""
GET_NODES_AND_APS_QUERY = """
SELECT m.name, n.name, n.description, n.mac, n.hardware, n.ip, n.last_contact, n.lat, n.lon, n.created, n.config_fetched, n.last_contact_from_ip
FROM nodes n
JOIN meshes m
ON n.mesh_id = m.id;
SELECT null,   a.name, a.description, a.mac, a.hardware, null, a.last_contact, a.lat, a.lon, a.created, a.config_fetched, a.last_contact_from_ip
FROM aps a;
"""
GET_NODE_AND_AP_STATIONS_QUERY = """
SELECT n.mac, s.radio_number, s.frequency_band, s.mac, s.tx_bytes, s.rx_bytes, s.tx_packets, s.rx_packets, s.tx_bitrate, s.rx_bitrate, s.tx_failed, s.tx_retries, s.signal_now, s.signal_avg, s.created, s.id
FROM node_stations s
JOIN nodes n
ON s.node_id = n.id;
SELECT a.mac, s.radio_number, s.frequency_band, s.mac, s.tx_bytes, s.rx_bytes, s.tx_packets, s.rx_packets, s.tx_bitrate, s.rx_bitrate, s.tx_failed, s.tx_retries, s.signal_now, s.signal_avg, s.created, s.id
FROM ap_stations s
JOIN aps a
ON s.ap_id = a.id;
"""
GET_NODE_AND_AP_LOADS_QUERY = """
SELECT n.mac, l.mem_total, l.mem_free, l.uptime, l.system_time, l.created, l.id
FROM node_loads l
JOIN nodes n
ON l.node_id = n.id;
SELECT a.mac, l.mem_total, l.mem_free, l.uptime, l.system_time, l.created, l.id
FROM ap_loads l
JOIN aps a
ON l.ap_id = a.id;
"""
GET_NODE_AND_AP_UPTIME_HISTORY_QUERY = """
SELECT n.mac, h.node_state h.created, h.id
FROM node_uptm_histories h
JOIN nodes n
ON h.node_id = n.id;
SELECT a.mac, h.ap_state, h.id
FROM ap_uptm_histories h
JOIN aps a
ON h.ap_id = a.id;
"""


def bulk_sync(ModelType, delete=True):
    """Log output for sync, with number of added, updated and deleted models."""

    def outer(syncfunc):
        def inner(cursor):
            ids_to_delete = set(ModelType.objects.values_list("pk", flat=True))
            n_added, n_updated = 0, 0
            for defaults, kwargs in syncfunc(cursor):
                model, created = ModelType.objects.update_or_create(defaults, **kwargs)
                if created:
                    n_added += 1
                else:
                    n_updated += 1
                ids_to_delete.discard(model.pk)
            n_deleted = 0
            if delete:
                n_deleted, _ = ModelType.objects.filter(pk__in=ids_to_delete).delete()
            print(
                f"Updated {ModelType.__name__:>12} models ({n_added} created, {n_updated} updated, {n_deleted} deleted)"
            )

        return inner

    return outer


@bulk_sync(Cloud)
def sync_clouds(cursor):
    cursor.execute(GET_CLOUDS_QUERY)
    for row in cursor.fetchall():
        data = dict(
            description=row[1],
            lat=row[2],
            lng=row[3],
            created=make_aware(row[4]),
        )
        yield data, {"name": row[0]}


@bulk_sync(Mesh)
def sync_meshes(cursor):
    cursor.execute(GET_MESHES_QUERY)
    for row in cursor.fetchall():
        data = dict(
            ssid=row[1],
            cloud=Cloud.objects.get(name=row[2]),
            created=make_aware(row[3]),
        )
        yield data, {"name": row[0]}


# The nodes that are out of sync mustn't be deleted, they can be potentially added to radiusdesk later
@bulk_sync(Node, delete=False)
def sync_nodes(cursor):
    for result in cursor.execute(GET_NODES_AND_APS_QUERY, multi=True):
        for row in result.fetchall():
            data = dict(
                mesh=Mesh.objects.get(name=row[0]) if row[0] else None,
                name=row[1],
                description=row[2],
                mac=row[3],
                hardware=row[4],
                ip=row[5],
                last_contact=make_aware(row[6]),
                # Don't want these to overwrite our values
                # lat=row[7],
                # lon=row[8],
                created=make_aware(row[9]),
                config_fetched=make_aware(row[10]),
                last_contact_from_ip=row[11],
            )
            yield data, {"name": row[1]}


@bulk_sync(NodeStation)
def sync_node_stations(cursor):
    for result in cursor.execute(GET_NODE_AND_AP_STATIONS_QUERY, multi=True):
        for row in result.fetchall():
            data = dict(
                node=Node.objects.get(mac=row[0]),
                radio_number=row[1],
                frequency_band=row[2],
                mac=row[3],
                tx_bytes=row[4],
                rx_bytes=row[5],
                tx_packets=row[6],
                rx_packets=row[7],
                tx_bitrate=row[8],
                rx_bitrate=row[9],
                tx_failed=row[10],
                tx_retries=row[11],
                signal_now=row[12],
                signal_avg=row[13],
                created=make_aware(row[14]),
            )
            yield data, {"pk": row[15]}


@bulk_sync(NodeLoad)
def sync_node_loads(cursor):
    for result in cursor.execute(GET_NODE_AND_AP_LOADS_QUERY, multi=True):
        for row in result.fetchall():
            data = dict(
                node=Node.objects.get(mac=row[0]),
                mem_total=row[1],
                mem_free=row[2],
                uptime=row[3],
                system_time=row[4],
                created=make_aware(row[5]),
            )
            yield data, {"pk": row[6]}


@bulk_sync(UptimeMetric)
def sync_node_uptime_metrics(cursor):
    for result in cursor.execute(GET_NODE_AND_AP_UPTIME_HISTORY_QUERY, multi=True):
        for row in result.fetchall():
            data = dict(
                node=Node.objects.get(mac=row[0]),
                reachable=row[1],
                loss=0 if row[1] else 100,
                created=make_aware(row[2]),
            )
            yield data, {"pk": row[5]}


def run():
    with connect(
        host=settings.RD_DB_HOST,
        user=settings.RD_DB_USER,
        password=settings.RD_DB_PASSWORD,
        database=settings.RD_DB_NAME,
        port=settings.RD_DB_PORT,
    ) as connection:
        with connection.cursor() as cursor:
            start_time = time.time()
            sync_clouds(cursor)
            sync_meshes(cursor)
            sync_nodes(cursor)
            sync_node_stations(cursor)
            sync_node_loads(cursor)
            # sync_node_uptime_metrics(cursor)
            elapsed_time = time.time() - start_time
            print(f"Synced with radiusdesk in {elapsed_time:.2f}s")
