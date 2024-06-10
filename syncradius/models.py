# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccelArrivals(models.Model):
    mac = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_contact_from_ip = models.CharField(max_length=30)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_arrivals'


class AccelProfileEntries(models.Model):
    accel_profile_id = models.IntegerField()
    section = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    no_key_flag = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_profile_entries'


class AccelProfiles(models.Model):
    cloud_id = models.IntegerField()
    name = models.CharField(max_length=255)
    base_config = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_profiles'


class AccelServers(models.Model):
    cloud_id = models.IntegerField()
    accel_profile_id = models.IntegerField()
    name = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    pppoe_interface = models.CharField(max_length=10)
    nas_identifier = models.CharField(max_length=32)
    server_type = models.CharField(max_length=10, blank=True, null=True)
    config_fetched = models.DateTimeField(blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_contact_from_ip = models.CharField(max_length=30)
    restart_service_flag = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_servers'


class AccelSessions(models.Model):
    accel_server_id = models.IntegerField()
    netns = models.CharField(max_length=255)
    vrf = models.CharField(max_length=255)
    ifname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    ip = models.CharField(max_length=32)
    ip6 = models.CharField(max_length=32)
    ip6_dp = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    uptime = models.CharField(max_length=32)
    uptime_raw = models.IntegerField()
    calling_sid = models.CharField(max_length=32)
    called_sid = models.CharField(max_length=32)
    sid = models.CharField(max_length=32)
    comp = models.CharField(max_length=32)
    rx_bytes = models.CharField(max_length=32)
    tx_bytes = models.CharField(max_length=32)
    rx_bytes_raw = models.IntegerField()
    tx_bytes_raw = models.IntegerField()
    rx_pkts = models.IntegerField()
    tx_pkts = models.IntegerField()
    inbound_if = models.CharField(max_length=32)
    service_name = models.CharField(max_length=32)
    rate_limit = models.CharField(max_length=32)
    disconnect_flag = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_sessions'


class AccelStats(models.Model):
    accel_server_id = models.IntegerField()
    version = models.CharField(max_length=255)
    uptime = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    mem = models.CharField(max_length=255)
    core = models.TextField()
    sessions_active = models.IntegerField()
    sessions = models.TextField()
    pppoe = models.TextField()
    radius1 = models.TextField()
    radius2 = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accel_stats'


class Actions(models.Model):
    na_id = models.IntegerField()
    action = models.CharField(max_length=7, blank=True, null=True)
    command = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actions'


class Alerts(models.Model):
    description = models.CharField(max_length=255)
    node_id = models.IntegerField(blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    ap_id = models.IntegerField(blank=True, null=True)
    ap_profile_id = models.IntegerField(blank=True, null=True)
    detected = models.DateTimeField()
    acknowledged = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    resolved = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alerts'


class ApActions(models.Model):
    ap_id = models.IntegerField()
    action = models.CharField(max_length=17, blank=True, null=True)
    command = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    reply = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ap_actions'


class ApApProfileEntries(models.Model):
    ap_id = models.IntegerField()
    ap_profile_entry_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_ap_profile_entries'


class ApConnectionSettings(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    grouping = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    value = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_connection_settings'


class ApLoads(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    mem_total = models.IntegerField(blank=True, null=True)
    mem_free = models.IntegerField(blank=True, null=True)
    uptime = models.CharField(max_length=255, blank=True, null=True)
    system_time = models.CharField(max_length=255)
    load_1 = models.FloatField()
    load_2 = models.FloatField()
    load_3 = models.FloatField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_loads'


class ApProfileEntries(models.Model):
    ap_profile_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    hidden = models.IntegerField()
    isolate = models.IntegerField()
    encryption = models.CharField(max_length=4, blank=True, null=True)
    special_key = models.CharField(max_length=100)
    auth_server = models.CharField(max_length=255)
    auth_secret = models.CharField(max_length=255)
    dynamic_vlan = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    chk_maxassoc = models.IntegerField()
    maxassoc = models.IntegerField(blank=True, null=True)
    macfilter = models.CharField(max_length=7, blank=True, null=True)
    permanent_user_id = models.IntegerField()
    nasid = models.CharField(max_length=255)
    auto_nasid = models.IntegerField()
    accounting = models.IntegerField()
    default_vlan = models.IntegerField()
    default_key = models.CharField(max_length=255)
    hotspot2_enable = models.IntegerField()
    hotspot2_profile_id = models.IntegerField(blank=True, null=True)
    ieee802r = models.IntegerField()
    mobility_domain = models.CharField(max_length=4)
    ft_over_ds = models.IntegerField()
    ft_pskgenerate_local = models.IntegerField()
    apply_to_all = models.IntegerField()
    realm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ap_profile_entries'


class ApProfileEntrySchedules(models.Model):
    ap_profile_entry_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=3, blank=True, null=True)
    mo = models.IntegerField()
    tu = models.IntegerField()
    we = models.IntegerField()
    th = models.IntegerField()
    fr = models.IntegerField()
    sa = models.IntegerField()
    su = models.IntegerField()
    event_time = models.CharField(max_length=10)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_profile_entry_schedules'


class ApProfileExitApProfileEntries(models.Model):
    ap_profile_exit_id = models.IntegerField()
    ap_profile_entry_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_profile_exit_ap_profile_entries'


class ApProfileExitCaptivePortals(models.Model):
    ap_profile_exit_id = models.IntegerField()
    radius_1 = models.CharField(max_length=128)
    radius_2 = models.CharField(max_length=128)
    radius_secret = models.CharField(max_length=128)
    radius_nasid = models.CharField(max_length=128)
    uam_url = models.CharField(max_length=255)
    uam_secret = models.CharField(max_length=255)
    walled_garden = models.CharField(max_length=255)
    swap_octets = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    mac_auth = models.IntegerField()
    proxy_enable = models.IntegerField()
    proxy_ip = models.CharField(max_length=128)
    proxy_port = models.IntegerField()
    proxy_auth_username = models.CharField(max_length=128)
    proxy_auth_password = models.CharField(max_length=128)
    coova_optional = models.CharField(max_length=255)
    dns_manual = models.IntegerField()
    dns1 = models.CharField(max_length=128)
    dns2 = models.CharField(max_length=128)
    uamanydns = models.IntegerField()
    dnsparanoia = models.IntegerField()
    dnsdesk = models.IntegerField()
    ap_profile_exit_upstream_id = models.IntegerField(blank=True, null=True)
    softflowd_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ap_profile_exit_captive_portals'


class ApProfileExitPppoeServers(models.Model):
    ap_profile_exit_id = models.IntegerField()
    accel_profile_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_profile_exit_pppoe_servers'


class ApProfileExitSettings(models.Model):
    ap_profile_exit_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_profile_exit_settings'


class ApProfileExits(models.Model):
    ap_profile_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    vlan = models.IntegerField(blank=True, null=True)
    auto_dynamic_client = models.IntegerField()
    realm_list = models.CharField(max_length=128)
    auto_login_page = models.IntegerField()
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    openvpn_server_id = models.IntegerField(blank=True, null=True)
    proto = models.CharField(max_length=6, blank=True, null=True)
    ipaddr = models.CharField(max_length=50)
    netmask = models.CharField(max_length=50)
    gateway = models.CharField(max_length=50)
    dns_1 = models.CharField(max_length=50)
    dns_2 = models.CharField(max_length=50)
    apply_firewall_profile = models.IntegerField()
    firewall_profile_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ap_profile_exits'


class ApProfileSettings(models.Model):
    ap_profile_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    heartbeat_interval = models.IntegerField()
    heartbeat_dead_after = models.IntegerField()
    password_hash = models.CharField(max_length=100)
    tz_name = models.CharField(max_length=128)
    tz_value = models.CharField(max_length=128)
    country = models.CharField(max_length=5)
    gw_dhcp_timeout = models.IntegerField()
    gw_use_previous = models.IntegerField()
    gw_auto_reboot = models.IntegerField()
    gw_auto_reboot_time = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    syslog1_ip = models.CharField(max_length=50)
    syslog1_port = models.CharField(max_length=10)
    syslog2_ip = models.CharField(max_length=50)
    syslog2_port = models.CharField(max_length=10)
    syslog3_ip = models.CharField(max_length=50)
    syslog3_port = models.CharField(max_length=10)
    report_adv_enable = models.IntegerField()
    report_adv_proto = models.CharField(max_length=5, blank=True, null=True)
    report_adv_light = models.IntegerField(blank=True, null=True)
    report_adv_full = models.IntegerField(blank=True, null=True)
    report_adv_sampling = models.IntegerField(blank=True, null=True)
    enable_schedules = models.IntegerField()
    schedule_id = models.IntegerField(blank=True, null=True)
    vlan_enable = models.IntegerField()
    vlan_range_or_list = models.CharField(max_length=5, blank=True, null=True)
    vlan_start = models.IntegerField()
    vlan_end = models.IntegerField()
    vlan_list = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ap_profile_settings'


class ApProfileSpecifics(models.Model):
    ap_profile_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_profile_specifics'


class ApProfiles(models.Model):
    name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    enable_alerts = models.IntegerField()
    enable_overviews = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ap_profiles'


class ApStaticEntryOverrides(models.Model):
    ap_id = models.IntegerField()
    ap_profile_entry_id = models.IntegerField()
    item = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_static_entry_overrides'


class ApStations(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    ap_profile_entry_id = models.IntegerField(blank=True, null=True)
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.BigIntegerField()
    rx_packets = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    authenticated = models.IntegerField()
    authorized = models.IntegerField()
    tdls_peer = models.IntegerField()
    preamble = models.CharField(max_length=255)
    tx_failed = models.IntegerField()
    wmm_wme = models.IntegerField()
    tx_retries = models.IntegerField()
    mfp = models.IntegerField()
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_stations'


class ApSystems(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_systems'


class ApUptmHistories(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    ap_state = models.IntegerField()
    state_datetime = models.DateTimeField()
    report_datetime = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_uptm_histories'


class ApWifiSettings(models.Model):
    ap_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ap_wifi_settings'


class AppliedFupComponents(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    profile_fup_component_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'applied_fup_components'


class Aps(models.Model):
    ap_profile_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    hardware = models.CharField(max_length=255, blank=True, null=True)
    last_contact_from_ip = models.CharField(max_length=255, blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    on_public_maps = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    photo_file_name = models.CharField(max_length=128)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    config_fetched = models.DateTimeField(blank=True, null=True)
    lan_proto = models.CharField(max_length=30)
    lan_ip = models.CharField(max_length=30)
    lan_gw = models.CharField(max_length=30)
    gateway = models.CharField(max_length=11, blank=True, null=True)
    reboot_flag = models.IntegerField()
    tree_tag_id = models.IntegerField(blank=True, null=True)
    enable_alerts = models.IntegerField()
    enable_overviews = models.IntegerField()
    enable_schedules = models.IntegerField()
    schedule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aps'


class ArMeshDailySummaries(models.Model):
    id = models.IntegerField(primary_key=True)
    mesh_id = models.IntegerField()
    the_date = models.DateField()
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    min_clients = models.BigIntegerField(blank=True, null=True)
    max_clients = models.BigIntegerField(blank=True, null=True)
    min_nodes = models.BigIntegerField(blank=True, null=True)
    max_nodes = models.BigIntegerField(blank=True, null=True)
    min_lv_nodes = models.BigIntegerField(blank=True, null=True)
    max_lv_nodes = models.BigIntegerField(blank=True, null=True)
    min_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    max_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    min_nodes_down = models.BigIntegerField(blank=True, null=True)
    max_nodes_down = models.BigIntegerField(blank=True, null=True)
    min_nodes_up = models.BigIntegerField(blank=True, null=True)
    max_nodes_up = models.BigIntegerField(blank=True, null=True)
    min_dual_radios = models.BigIntegerField(blank=True, null=True)
    max_dual_radios = models.BigIntegerField(blank=True, null=True)
    min_single_radios = models.BigIntegerField(blank=True, null=True)
    max_single_radios = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_mesh_daily_summaries'
        unique_together = (('mesh_id', 'the_date'),)


class ArNodeIbssConnections(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField(blank=True, null=True)
    station_node_id = models.IntegerField(blank=True, null=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.IntegerField()
    rx_packets = models.IntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    tx_extra_info = models.CharField(max_length=255)
    rx_extra_info = models.CharField(max_length=255)
    authenticated = models.CharField(max_length=3, blank=True, null=True)
    authorized = models.CharField(max_length=3, blank=True, null=True)
    tdls_peer = models.CharField(max_length=255)
    preamble = models.CharField(max_length=5, blank=True, null=True)
    tx_failed = models.IntegerField()
    inactive_time = models.IntegerField()
    wmm_wme = models.CharField(db_column='WMM_WME', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tx_retries = models.IntegerField()
    mfp = models.CharField(db_column='MFP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_node_ibss_connections'


class ArNodeStations(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField(blank=True, null=True)
    mesh_entry_id = models.IntegerField(blank=True, null=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.IntegerField()
    rx_packets = models.IntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    tx_extra_info = models.CharField(max_length=255)
    rx_extra_info = models.CharField(max_length=255)
    authenticated = models.CharField(max_length=3, blank=True, null=True)
    authorized = models.CharField(max_length=3, blank=True, null=True)
    tdls_peer = models.CharField(max_length=255)
    preamble = models.CharField(max_length=5, blank=True, null=True)
    tx_failed = models.IntegerField()
    inactive_time = models.IntegerField()
    wmm_wme = models.CharField(db_column='WMM_WME', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tx_retries = models.IntegerField()
    mfp = models.CharField(db_column='MFP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_node_stations'


class ArNodeUptmHistories(models.Model):
    id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField(blank=True, null=True)
    node_state = models.IntegerField()
    state_datetime = models.DateTimeField()
    report_datetime = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_node_uptm_histories'


class AutoDevices(models.Model):
    mac = models.CharField(primary_key=True, max_length=17)
    username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auto_devices'


class Checks(models.Model):
    name = models.CharField(max_length=40)
    value = models.CharField(max_length=40)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checks'


class ClientMacs(models.Model):
    mac = models.CharField(unique=True, max_length=17, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_macs'


class CloudAdmins(models.Model):
    cloud_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cloud_admins'


class CloudSettings(models.Model):
    cloud_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cloud_settings'


class Clouds(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clouds'


class CoaRequests(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    multiple_gateways = models.IntegerField()
    avp_json = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    request_type = models.CharField(max_length=3, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coa_requests'


class Countries(models.Model):
    name = models.CharField(max_length=64)
    alpha_2_code = models.CharField(max_length=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'countries'


class DataCollectorOtps(models.Model):
    data_collector_id = models.IntegerField()
    status = models.CharField(max_length=13, blank=True, null=True)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_collector_otps'


class DataCollectors(models.Model):
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    mac = models.CharField(max_length=36)
    cp_mac = models.CharField(max_length=36, blank=True, null=True)
    public_ip = models.CharField(max_length=36, blank=True, null=True)
    nasid = models.CharField(max_length=255, blank=True, null=True)
    ssid = models.CharField(max_length=255, blank=True, null=True)
    is_mobile = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    phone = models.CharField(max_length=36)
    dn = models.CharField(max_length=36)
    phone_opt_in = models.IntegerField()
    email_opt_in = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=12, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    custom1 = models.CharField(max_length=50)
    custom2 = models.CharField(max_length=50)
    custom3 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'data_collectors'


class Devices(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    active = models.IntegerField()
    last_accept_time = models.DateTimeField(blank=True, null=True)
    last_reject_time = models.DateTimeField(blank=True, null=True)
    last_accept_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_message = models.CharField(max_length=255, blank=True, null=True)
    permanent_user_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    perc_time_used = models.IntegerField(blank=True, null=True)
    perc_data_used = models.IntegerField(blank=True, null=True)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)
    time_cap_type = models.CharField(max_length=4, blank=True, null=True)
    data_cap_type = models.CharField(max_length=4, blank=True, null=True)
    realm = models.CharField(max_length=100)
    realm_id = models.IntegerField(blank=True, null=True)
    profile = models.CharField(max_length=100)
    profile_id = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class DynamicClientMacs(models.Model):
    dynamic_client_id = models.IntegerField(blank=True, null=True)
    client_mac_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_client_macs'
        unique_together = (('dynamic_client_id', 'client_mac_id'),)


class DynamicClientRealms(models.Model):
    dynamic_client_id = models.IntegerField()
    realm_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_client_realms'


class DynamicClientSettings(models.Model):
    dynamic_client_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_client_settings'


class DynamicClientStates(models.Model):
    dynamic_client_id = models.CharField(max_length=36)
    state = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_client_states'


class DynamicClients(models.Model):
    name = models.CharField(max_length=64)
    nasidentifier = models.CharField(max_length=128)
    calledstationid = models.CharField(max_length=128)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_contact_ip = models.CharField(max_length=128)
    timezone = models.CharField(max_length=255)
    monitor = models.CharField(max_length=9, blank=True, null=True)
    session_auto_close = models.IntegerField()
    session_dead_time = models.IntegerField()
    active = models.IntegerField()
    on_public_maps = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    photo_file_name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    data_limit_active = models.IntegerField()
    data_limit_amount = models.FloatField()
    data_limit_unit = models.CharField(max_length=2, blank=True, null=True)
    data_limit_reset_on = models.IntegerField()
    data_limit_reset_hour = models.IntegerField()
    data_limit_reset_minute = models.IntegerField()
    data_used = models.BigIntegerField(blank=True, null=True)
    data_limit_cap = models.CharField(max_length=4, blank=True, null=True)
    daily_data_limit_active = models.IntegerField()
    daily_data_limit_amount = models.FloatField()
    daily_data_limit_unit = models.CharField(max_length=2, blank=True, null=True)
    daily_data_limit_cap = models.CharField(max_length=4, blank=True, null=True)
    daily_data_limit_reset_hour = models.IntegerField()
    daily_data_limit_reset_minute = models.IntegerField()
    daily_data_used = models.BigIntegerField(blank=True, null=True)
    default_vlan = models.IntegerField()
    default_key = models.CharField(max_length=255)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_clients'


class DynamicDetailCtcs(models.Model):
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    connect_check = models.IntegerField()
    connect_username = models.CharField(max_length=50)
    connect_suffix = models.CharField(max_length=50)
    connect_delay = models.IntegerField()
    connect_only = models.IntegerField()
    cust_info_check = models.IntegerField()
    ci_resupply_interval = models.IntegerField()
    ci_first_name = models.IntegerField()
    ci_first_name_required = models.IntegerField()
    ci_last_name = models.IntegerField()
    ci_last_name_required = models.IntegerField()
    ci_email = models.IntegerField()
    ci_email_required = models.IntegerField()
    ci_email_opt_in = models.IntegerField()
    ci_email_opt_in_txt = models.CharField(max_length=50)
    ci_gender = models.IntegerField()
    ci_gender_required = models.IntegerField()
    ci_birthday = models.IntegerField()
    ci_birthday_required = models.IntegerField()
    ci_company = models.IntegerField()
    ci_company_required = models.IntegerField()
    ci_address = models.IntegerField()
    ci_address_required = models.IntegerField()
    ci_city = models.IntegerField()
    ci_city_required = models.IntegerField()
    ci_country = models.IntegerField()
    ci_country_required = models.IntegerField()
    ci_phone = models.IntegerField()
    ci_phone_required = models.IntegerField()
    ci_phone_opt_in = models.IntegerField()
    ci_phone_opt_in_txt = models.CharField(max_length=50)
    ci_room = models.IntegerField()
    ci_room_required = models.IntegerField()
    ci_custom1 = models.IntegerField()
    ci_custom1_required = models.IntegerField()
    ci_custom1_txt = models.CharField(max_length=50)
    ci_custom2 = models.IntegerField()
    ci_custom2_required = models.IntegerField()
    ci_custom2_txt = models.CharField(max_length=50)
    ci_custom3 = models.IntegerField()
    ci_custom3_required = models.IntegerField()
    ci_custom3_txt = models.CharField(max_length=50)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    ci_phone_otp = models.IntegerField()
    ci_email_otp = models.IntegerField()
    permanent_user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_detail_ctcs'


class DynamicDetailLanguages(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_detail_languages'


class DynamicDetailMobiles(models.Model):
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    mobile_only = models.IntegerField()
    content = models.TextField()
    android_enable = models.IntegerField()
    android_href = models.CharField(max_length=255)
    android_text = models.CharField(max_length=255)
    android_content = models.TextField()
    apple_enable = models.IntegerField()
    apple_href = models.CharField(max_length=255)
    apple_text = models.CharField(max_length=255)
    apple_content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_detail_mobiles'


class DynamicDetailPrelogins(models.Model):
    mac = models.CharField(max_length=64)
    nasid = models.CharField(max_length=64)
    dynamic_detail_id = models.IntegerField()
    completed = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_detail_prelogins'


class DynamicDetailSocialLogins(models.Model):
    dynamic_detail_id = models.IntegerField()
    profile_id = models.IntegerField()
    realm_id = models.IntegerField()
    name = models.CharField(max_length=50)
    enable = models.IntegerField()
    record_info = models.IntegerField()
    special_key = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)
    type = models.CharField(max_length=7, blank=True, null=True)
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_detail_social_logins'


class DynamicDetailTransKeys(models.Model):
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_detail_trans_keys'


class DynamicDetailTranslations(models.Model):
    dynamic_detail_language_id = models.IntegerField(blank=True, null=True)
    dynamic_detail_trans_key_id = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_detail_translations'


class DynamicDetails(models.Model):
    name = models.CharField(max_length=64)
    icon_file_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=14)
    cell = models.CharField(max_length=14)
    email = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    street_no = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    town_suburb = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    t_c_check = models.IntegerField()
    t_c_url = models.CharField(max_length=50)
    redirect_check = models.IntegerField()
    redirect_url = models.CharField(max_length=200)
    slideshow_check = models.IntegerField()
    seconds_per_slide = models.IntegerField()
    connect_check = models.IntegerField()
    connect_username = models.CharField(max_length=50)
    connect_suffix = models.CharField(max_length=50)
    connect_delay = models.IntegerField()
    connect_only = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    user_login_check = models.IntegerField()
    voucher_login_check = models.IntegerField()
    auto_suffix_check = models.IntegerField()
    auto_suffix = models.CharField(max_length=200)
    usage_show_check = models.IntegerField()
    usage_refresh_interval = models.IntegerField()
    theme = models.CharField(max_length=200)
    register_users = models.IntegerField()
    lost_password = models.IntegerField()
    social_enable = models.IntegerField()
    social_temp_permanent_user_id = models.IntegerField(blank=True, null=True)
    coova_desktop_url = models.CharField(max_length=255)
    coova_mobile_url = models.CharField(max_length=255)
    mikrotik_desktop_url = models.CharField(max_length=255)
    mikrotik_mobile_url = models.CharField(max_length=255)
    default_language = models.CharField(max_length=255)
    realm_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    reg_auto_suffix_check = models.IntegerField()
    reg_auto_suffix = models.CharField(max_length=200)
    reg_mac_check = models.IntegerField()
    reg_auto_add = models.IntegerField()
    reg_email = models.IntegerField()
    slideshow_enforce_watching = models.IntegerField()
    slideshow_enforce_seconds = models.IntegerField()
    available_languages = models.CharField(max_length=255)
    ctc_require_email = models.IntegerField()
    ctc_resupply_email_interval = models.IntegerField()
    show_screen_delay = models.IntegerField()
    show_logo = models.IntegerField()
    show_name = models.IntegerField()
    name_colour = models.CharField(max_length=255)
    lost_password_method = models.CharField(max_length=5, blank=True, null=True)
    ctc_phone_opt_in = models.IntegerField()
    ctc_phone_opt_in_txt = models.CharField(max_length=200)
    ctc_email_opt_in = models.IntegerField()
    ctc_email_opt_in_txt = models.CharField(max_length=200)
    chilli_json_unavailable = models.IntegerField()
    chilli_use_chap = models.IntegerField()
    reg_otp_sms = models.IntegerField()
    reg_otp_email = models.IntegerField()
    permanent_user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_details'


class DynamicPages(models.Model):
    dynamic_detail_id = models.IntegerField()
    name = models.CharField(max_length=128)
    content = models.TextField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    dynamic_detail_language_id = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_pages'


class DynamicPairs(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    priority = models.IntegerField()
    dynamic_detail_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_pairs'


class DynamicPhotoTranslations(models.Model):
    dynamic_detail_language_id = models.IntegerField(blank=True, null=True)
    dynamic_photo_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dynamic_photo_translations'


class DynamicPhotos(models.Model):
    dynamic_detail_id = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    file_name = models.CharField(max_length=128)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()
    fit = models.CharField(max_length=14, blank=True, null=True)
    background_color = models.CharField(max_length=7)
    slide_duration = models.IntegerField()
    include_title = models.IntegerField()
    include_description = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynamic_photos'


class EmailHistories(models.Model):
    cloud_id = models.IntegerField()
    recipient = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=25, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_histories'


class EmailMessages(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    message = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_messages'


class FirewallApps(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    fa_code = models.CharField(max_length=64, blank=True, null=True)
    elements = models.TextField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firewall_apps'


class FirewallProfileEntries(models.Model):
    firewall_profile_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=5, blank=True, null=True)
    category = models.CharField(max_length=13, blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    schedule = models.CharField(max_length=10, blank=True, null=True)
    mo = models.IntegerField()
    tu = models.IntegerField()
    we = models.IntegerField()
    th = models.IntegerField()
    fr = models.IntegerField()
    sa = models.IntegerField()
    su = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    one_time_date = models.DateTimeField(blank=True, null=True)
    bw_up = models.IntegerField(blank=True, null=True)
    bw_down = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firewall_profile_entries'


class FirewallProfileEntryFirewallApps(models.Model):
    firewall_profile_entry_id = models.IntegerField()
    firewall_app_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firewall_profile_entry_firewall_apps'


class FirewallProfiles(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'firewall_profiles'


class ForwardLookups(models.Model):
    fqdn = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forward_lookups'


class Groups(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class HardwareRadios(models.Model):
    radio_number = models.IntegerField()
    disabled = models.IntegerField()
    txpower = models.IntegerField()
    include_beacon_int = models.IntegerField()
    beacon_int = models.IntegerField()
    include_distance = models.IntegerField()
    distance = models.IntegerField()
    ht_capab = models.CharField(max_length=255, blank=True, null=True)
    mesh = models.IntegerField()
    ap = models.IntegerField()
    config = models.IntegerField()
    hardware_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    band = models.CharField(max_length=2, blank=True, null=True)
    mode = models.CharField(max_length=2, blank=True, null=True)
    width = models.CharField(max_length=3, blank=True, null=True)
    cell_density = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware_radios'


class Hardwares(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    fw_id = models.CharField(max_length=20)
    for_mesh = models.IntegerField()
    for_ap = models.IntegerField()
    wan = models.CharField(max_length=20)
    lan = models.CharField(max_length=20, blank=True, null=True)
    radio_count = models.IntegerField()
    photo_file_name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hardwares'


class HomeServerPools(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=19, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_server_pools'


class HomeServers(models.Model):
    type = models.CharField(max_length=9, blank=True, null=True)
    ipaddr = models.CharField(max_length=255)
    port = models.IntegerField()
    secret = models.CharField(max_length=255)
    response_window = models.IntegerField()
    zombie_period = models.IntegerField()
    revive_interval = models.IntegerField()
    home_server_pool_id = models.IntegerField(blank=True, null=True)
    accept_coa = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_servers'


class IspSpecifics(models.Model):
    cloud_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    region = models.CharField(max_length=40, blank=True, null=True)
    field1 = models.CharField(max_length=40, blank=True, null=True)
    field2 = models.CharField(max_length=40, blank=True, null=True)
    field3 = models.CharField(max_length=40, blank=True, null=True)
    field4 = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'isp_specifics'


class Languages(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    iso_code = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class MacActions(models.Model):
    cloud_id = models.IntegerField(blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    ap_profile_id = models.IntegerField(blank=True, null=True)
    client_mac_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=8, blank=True, null=True)
    bw_up = models.IntegerField(blank=True, null=True)
    bw_down = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    firewall_profile_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_actions'


class MacAliases(models.Model):
    mac = models.CharField(max_length=20, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mac_aliases'


class MacUsages(models.Model):
    mac = models.CharField(max_length=17)
    username = models.CharField(max_length=255)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mac_usages'


class MeshDailySummaries(models.Model):
    mesh_id = models.IntegerField()
    the_date = models.DateField()
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    min_clients = models.BigIntegerField(blank=True, null=True)
    max_clients = models.BigIntegerField(blank=True, null=True)
    min_nodes = models.BigIntegerField(blank=True, null=True)
    max_nodes = models.BigIntegerField(blank=True, null=True)
    min_lv_nodes = models.BigIntegerField(blank=True, null=True)
    max_lv_nodes = models.BigIntegerField(blank=True, null=True)
    min_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    max_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    min_nodes_down = models.BigIntegerField(blank=True, null=True)
    max_nodes_down = models.BigIntegerField(blank=True, null=True)
    min_nodes_up = models.BigIntegerField(blank=True, null=True)
    max_nodes_up = models.BigIntegerField(blank=True, null=True)
    min_dual_radios = models.BigIntegerField(blank=True, null=True)
    max_dual_radios = models.BigIntegerField(blank=True, null=True)
    min_single_radios = models.BigIntegerField(blank=True, null=True)
    max_single_radios = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_daily_summaries'
        unique_together = (('mesh_id', 'the_date'),)


class MeshEntries(models.Model):
    mesh_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    hidden = models.IntegerField()
    isolate = models.IntegerField()
    apply_to_all = models.IntegerField()
    encryption = models.CharField(max_length=4, blank=True, null=True)
    special_key = models.CharField(max_length=100)
    auth_server = models.CharField(max_length=255)
    auth_secret = models.CharField(max_length=255)
    dynamic_vlan = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    chk_maxassoc = models.IntegerField()
    maxassoc = models.IntegerField(blank=True, null=True)
    macfilter = models.CharField(max_length=7, blank=True, null=True)
    permanent_user_id = models.IntegerField()
    nasid = models.CharField(max_length=255)
    auto_nasid = models.IntegerField()
    accounting = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    default_vlan = models.IntegerField()
    default_key = models.CharField(max_length=255)
    hotspot2_enable = models.IntegerField()
    hotspot2_profile_id = models.IntegerField(blank=True, null=True)
    ieee802r = models.IntegerField()
    mobility_domain = models.CharField(max_length=4)
    ft_over_ds = models.IntegerField()
    ft_pskgenerate_local = models.IntegerField()
    realm_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_entries'


class MeshEntrySchedules(models.Model):
    mesh_entry_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=3, blank=True, null=True)
    mo = models.IntegerField()
    tu = models.IntegerField()
    we = models.IntegerField()
    th = models.IntegerField()
    fr = models.IntegerField()
    sa = models.IntegerField()
    su = models.IntegerField()
    event_time = models.CharField(max_length=10)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mesh_entry_schedules'


class MeshExitCaptivePortals(models.Model):
    mesh_exit_id = models.IntegerField()
    radius_1 = models.CharField(max_length=128)
    radius_2 = models.CharField(max_length=128)
    radius_secret = models.CharField(max_length=128)
    radius_nasid = models.CharField(max_length=128)
    uam_url = models.CharField(max_length=255)
    uam_secret = models.CharField(max_length=255)
    walled_garden = models.CharField(max_length=255)
    swap_octets = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    mac_auth = models.IntegerField()
    proxy_enable = models.IntegerField()
    proxy_ip = models.CharField(max_length=128)
    proxy_port = models.IntegerField()
    proxy_auth_username = models.CharField(max_length=128)
    proxy_auth_password = models.CharField(max_length=128)
    coova_optional = models.CharField(max_length=255)
    dns_manual = models.IntegerField()
    dns1 = models.CharField(max_length=128)
    dns2 = models.CharField(max_length=128)
    uamanydns = models.IntegerField()
    dnsparanoia = models.IntegerField()
    dnsdesk = models.IntegerField()
    mesh_exit_upstream_id = models.IntegerField(blank=True, null=True)
    softflowd_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesh_exit_captive_portals'


class MeshExitMeshEntries(models.Model):
    mesh_exit_id = models.IntegerField()
    mesh_entry_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mesh_exit_mesh_entries'


class MeshExitPppoeServers(models.Model):
    mesh_exit_id = models.IntegerField()
    accel_profile_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mesh_exit_pppoe_servers'


class MeshExitSettings(models.Model):
    mesh_exit_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mesh_exit_settings'


class MeshExits(models.Model):
    mesh_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=16, blank=True, null=True)
    auto_detect = models.IntegerField()
    vlan = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    openvpn_server_id = models.IntegerField(blank=True, null=True)
    proto = models.CharField(max_length=6, blank=True, null=True)
    ipaddr = models.CharField(max_length=50)
    netmask = models.CharField(max_length=50)
    gateway = models.CharField(max_length=50)
    dns_1 = models.CharField(max_length=50)
    dns_2 = models.CharField(max_length=50)
    apply_firewall_profile = models.IntegerField()
    firewall_profile_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mesh_exits'


class MeshSettings(models.Model):
    mesh_id = models.IntegerField(blank=True, null=True)
    aggregated_ogms = models.IntegerField()
    ap_isolation = models.IntegerField()
    bonding = models.IntegerField()
    bridge_loop_avoidance = models.IntegerField()
    fragmentation = models.IntegerField()
    distributed_arp_table = models.IntegerField()
    orig_interval = models.IntegerField()
    gw_sel_class = models.IntegerField()
    connectivity = models.CharField(max_length=10, blank=True, null=True)
    encryption = models.IntegerField()
    encryption_key = models.CharField(max_length=63)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    routing_algo = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesh_settings'


class MeshSpecifics(models.Model):
    mesh_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mesh_specifics'


class Meshes(models.Model):
    name = models.CharField(max_length=128)
    ssid = models.CharField(max_length=32)
    bssid = models.CharField(max_length=32)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    tree_tag_id = models.IntegerField(blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    enable_alerts = models.IntegerField()
    enable_overviews = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meshes'


class NaRealms(models.Model):
    na_id = models.IntegerField()
    realm_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'na_realms'


class NaSettings(models.Model):
    na_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'na_settings'


class NaStates(models.Model):
    na_id = models.CharField(max_length=36)
    state = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'na_states'


class Nas(models.Model):
    nasname = models.CharField(max_length=128)
    shortname = models.CharField(max_length=32, blank=True, null=True)
    nasidentifier = models.CharField(max_length=64)
    type = models.CharField(max_length=30, blank=True, null=True)
    ports = models.IntegerField(blank=True, null=True)
    secret = models.CharField(max_length=60)
    server = models.CharField(max_length=64, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    connection_type = models.CharField(max_length=7, blank=True, null=True)
    timezone = models.CharField(max_length=255)
    record_auth = models.IntegerField()
    ignore_acct = models.IntegerField()
    dynamic_attribute = models.CharField(max_length=50)
    dynamic_value = models.CharField(max_length=50)
    monitor = models.CharField(max_length=9, blank=True, null=True)
    ping_interval = models.IntegerField()
    heartbeat_dead_after = models.IntegerField()
    last_contact = models.DateTimeField(blank=True, null=True)
    session_auto_close = models.IntegerField()
    session_dead_time = models.IntegerField()
    on_public_maps = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    photo_file_name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nas'


class Networks(models.Model):
    name = models.CharField(max_length=64)
    site_id = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'networks'


class NewAccountings(models.Model):
    mac = models.CharField(primary_key=True, max_length=17)
    username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'new_accountings'


class NodeActions(models.Model):
    node_id = models.IntegerField()
    action = models.CharField(max_length=17, blank=True, null=True)
    command = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    reply = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_actions'


class NodeConnectionSettings(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    grouping = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    value = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_connection_settings'


class NodeIbssConnections(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    station_node_id = models.IntegerField(blank=True, null=True)
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    if_mac = models.CharField(max_length=17)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.BigIntegerField()
    rx_packets = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    authenticated = models.IntegerField()
    authorized = models.IntegerField()
    tdls_peer = models.IntegerField()
    preamble = models.CharField(max_length=255)
    tx_failed = models.IntegerField()
    wmm_wme = models.IntegerField()
    tx_retries = models.IntegerField()
    mfp = models.IntegerField()
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_ibss_connections'


class NodeIbssConnectionsDailies(models.Model):
    mac = models.CharField(max_length=64)
    mesh_id = models.IntegerField()
    node_id = models.IntegerField()
    station_node_id = models.IntegerField()
    if_mac = models.CharField(max_length=64)
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    signal_avg = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_ibss_connections_dailies'


class NodeLoads(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    mem_total = models.IntegerField(blank=True, null=True)
    mem_free = models.IntegerField(blank=True, null=True)
    uptime = models.CharField(max_length=255, blank=True, null=True)
    system_time = models.CharField(max_length=255)
    load_1 = models.FloatField()
    load_2 = models.FloatField()
    load_3 = models.FloatField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_loads'


class NodeMeshEntries(models.Model):
    node_id = models.IntegerField()
    mesh_entry_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_mesh_entries'


class NodeMeshExits(models.Model):
    node_id = models.IntegerField()
    mesh_exit_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_mesh_exits'


class NodeMpSettings(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_mp_settings'


class NodeNeighbors(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    gateway = models.CharField(max_length=3, blank=True, null=True)
    neighbor_id = models.IntegerField(blank=True, null=True)
    metric = models.DecimalField(max_digits=6, decimal_places=4)
    hwmode = models.CharField(max_length=5, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    algo = models.CharField(max_length=9, blank=True, null=True)
    tq = models.IntegerField(blank=True, null=True)
    tp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_neighbors'


class NodeScans(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    ap_id = models.IntegerField(blank=True, null=True)
    scan_data = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_scans'


class NodeSettings(models.Model):
    mesh_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    power = models.IntegerField()
    all_power = models.IntegerField()
    two_chan = models.IntegerField()
    five_chan = models.IntegerField()
    heartbeat_interval = models.IntegerField()
    heartbeat_dead_after = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    password_hash = models.CharField(max_length=100)
    eth_br_chk = models.IntegerField()
    eth_br_with = models.IntegerField()
    eth_br_for_all = models.IntegerField()
    tz_name = models.CharField(max_length=128)
    tz_value = models.CharField(max_length=128)
    country = models.CharField(max_length=5)
    gw_dhcp_timeout = models.IntegerField()
    gw_use_previous = models.IntegerField()
    gw_auto_reboot = models.IntegerField()
    gw_auto_reboot_time = models.IntegerField()
    client_key = models.CharField(max_length=255)
    syslog1_ip = models.CharField(max_length=50)
    syslog1_port = models.CharField(max_length=10)
    syslog2_ip = models.CharField(max_length=50)
    syslog2_port = models.CharField(max_length=10)
    syslog3_ip = models.CharField(max_length=50)
    syslog3_port = models.CharField(max_length=10)
    report_adv_enable = models.IntegerField()
    report_adv_proto = models.CharField(max_length=5, blank=True, null=True)
    report_adv_light = models.IntegerField(blank=True, null=True)
    report_adv_full = models.IntegerField(blank=True, null=True)
    report_adv_sampling = models.IntegerField(blank=True, null=True)
    enable_schedules = models.IntegerField()
    schedule_id = models.IntegerField(blank=True, null=True)
    vlan_enable = models.IntegerField()
    vlan_range_or_list = models.CharField(max_length=5, blank=True, null=True)
    vlan_start = models.IntegerField()
    vlan_end = models.IntegerField()
    vlan_list = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_settings'


class NodeStations(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    mesh_entry_id = models.IntegerField(blank=True, null=True)
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mac = models.CharField(max_length=17)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_packets = models.BigIntegerField()
    rx_packets = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    authenticated = models.IntegerField()
    authorized = models.IntegerField()
    tdls_peer = models.IntegerField()
    preamble = models.CharField(max_length=255)
    tx_failed = models.IntegerField()
    wmm_wme = models.IntegerField()
    tx_retries = models.IntegerField()
    mfp = models.IntegerField()
    signal_now = models.IntegerField()
    signal_avg = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_stations'


class NodeStationsDailies(models.Model):
    mac = models.CharField(max_length=64)
    node_station_id = models.IntegerField()
    mesh_id = models.IntegerField()
    mesh_entry_id = models.IntegerField()
    node_id = models.IntegerField()
    radio_number = models.IntegerField()
    frequency_band = models.CharField(max_length=10, blank=True, null=True)
    tx_bytes = models.BigIntegerField()
    rx_bytes = models.BigIntegerField()
    tx_bitrate = models.IntegerField()
    rx_bitrate = models.IntegerField()
    signal_avg = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_stations_dailies'


class NodeSystems(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_systems'


class NodeUptmHistories(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    node_state = models.IntegerField()
    state_datetime = models.DateTimeField()
    report_datetime = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_uptm_histories'


class NodeWifiSettings(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'node_wifi_settings'


class Nodes(models.Model):
    mesh_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    hardware = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    last_contact = models.DateTimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    config_fetched = models.DateTimeField(blank=True, null=True)
    lan_proto = models.CharField(max_length=30)
    lan_ip = models.CharField(max_length=30)
    lan_gw = models.CharField(max_length=30)
    last_contact_from_ip = models.CharField(max_length=30)
    mesh0 = models.CharField(max_length=25)
    mesh1 = models.CharField(max_length=25)
    mesh2 = models.CharField(max_length=25)
    gateway = models.CharField(max_length=11, blank=True, null=True)
    bootcycle = models.IntegerField()
    mesh0_frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mesh1_frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mesh2_frequency_band = models.CharField(max_length=10, blank=True, null=True)
    mesh0_channel = models.IntegerField()
    mesh1_channel = models.IntegerField()
    mesh2_channel = models.IntegerField()
    mesh0_txpower = models.IntegerField()
    mesh1_txpower = models.IntegerField()
    mesh2_txpower = models.IntegerField()
    reboot_flag = models.IntegerField()
    enable_alerts = models.IntegerField()
    enable_overviews = models.IntegerField()
    enable_schedules = models.IntegerField()
    schedule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes'


class Notifications(models.Model):
    severity = models.IntegerField()
    is_resolved = models.IntegerField()
    notification_datetime = models.DateTimeField()
    notification_type = models.CharField(max_length=32)
    notification_code = models.IntegerField()
    short_description = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_table = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notifications'


class OpenvpnClients(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    subnet = models.IntegerField(blank=True, null=True)
    peer1 = models.IntegerField(blank=True, null=True)
    peer2 = models.IntegerField(blank=True, null=True)
    na_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openvpn_clients'


class OpenvpnServerClients(models.Model):
    mesh_ap_profile = models.CharField(max_length=10, blank=True, null=True)
    openvpn_server_id = models.IntegerField(blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    mesh_exit_id = models.IntegerField(blank=True, null=True)
    ap_profile_id = models.IntegerField(blank=True, null=True)
    ap_profile_exit_id = models.IntegerField(blank=True, null=True)
    ap_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=40)
    last_contact_to_server = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openvpn_server_clients'


class OpenvpnServers(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    cloud_id = models.IntegerField(blank=True, null=True)
    local_remote = models.CharField(max_length=6, blank=True, null=True)
    protocol = models.CharField(max_length=3, blank=True, null=True)
    ip_address = models.CharField(max_length=40)
    port = models.IntegerField()
    vpn_gateway_address = models.CharField(max_length=40)
    vpn_bridge_start_address = models.CharField(max_length=40)
    vpn_mask = models.CharField(max_length=40)
    config_preset = models.CharField(max_length=100)
    ca_crt = models.TextField()
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'openvpn_servers'


class PermanentUserNotifications(models.Model):
    permanent_user_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    method = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    increment = models.IntegerField(blank=True, null=True)
    last_value = models.IntegerField(blank=True, null=True)
    last_notification = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permanent_user_notifications'


class PermanentUserOtps(models.Model):
    permanent_user_id = models.IntegerField()
    status = models.CharField(max_length=13, blank=True, null=True)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permanent_user_otps'


class PermanentUserSettings(models.Model):
    permanent_user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'permanent_user_settings'


class PermanentUsers(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    token = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    auth_type = models.CharField(max_length=128)
    active = models.IntegerField()
    last_accept_time = models.DateTimeField(blank=True, null=True)
    last_reject_time = models.DateTimeField(blank=True, null=True)
    last_accept_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_message = models.CharField(max_length=255, blank=True, null=True)
    perc_time_used = models.IntegerField(blank=True, null=True)
    perc_data_used = models.IntegerField(blank=True, null=True)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)
    time_cap_type = models.CharField(max_length=4, blank=True, null=True)
    data_cap_type = models.CharField(max_length=4, blank=True, null=True)
    realm = models.CharField(max_length=50)
    realm_id = models.IntegerField(blank=True, null=True)
    profile = models.CharField(max_length=50)
    profile_id = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    track_auth = models.IntegerField()
    track_acct = models.IntegerField()
    static_ip = models.CharField(max_length=50)
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    country_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    site = models.CharField(max_length=100)
    ppsk = models.CharField(max_length=100)
    realm_vlan_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permanent_users'


class PptpClients(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    na_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pptp_clients'


class PredefinedCommands(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    command = models.CharField(max_length=255)
    action = models.CharField(max_length=17, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'predefined_commands'


class ProfileComponents(models.Model):
    name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_components'


class ProfileFupComponents(models.Model):
    profile_id = models.IntegerField()
    name = models.CharField(max_length=255)
    if_condition = models.CharField(max_length=11, blank=True, null=True)
    time_start = models.CharField(max_length=255, blank=True, null=True)
    time_end = models.CharField(max_length=255, blank=True, null=True)
    data_amount = models.IntegerField(blank=True, null=True)
    data_unit = models.CharField(max_length=2, blank=True, null=True)
    action = models.CharField(max_length=14, blank=True, null=True)
    action_amount = models.IntegerField(blank=True, null=True)
    ip_pool = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profile_fup_components'


class Profiles(models.Model):
    name = models.CharField(max_length=128)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profiles'


class Radacct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(unique=True, max_length=32)
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.CharField(max_length=15)
    nasidentifier = models.CharField(max_length=64)
    nasportid = models.CharField(max_length=15, blank=True, null=True)
    nasporttype = models.CharField(max_length=32, blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctupdatetime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctinterval = models.IntegerField(blank=True, null=True)
    acctsessiontime = models.PositiveIntegerField(blank=True, null=True)
    acctauthentic = models.CharField(max_length=32, blank=True, null=True)
    connectinfo_start = models.CharField(max_length=50, blank=True, null=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.CharField(max_length=50)
    callingstationid = models.CharField(max_length=50)
    acctterminatecause = models.CharField(max_length=32)
    servicetype = models.CharField(max_length=32, blank=True, null=True)
    framedprotocol = models.CharField(max_length=32, blank=True, null=True)
    framedipaddress = models.CharField(max_length=15)
    acctstartdelay = models.IntegerField(blank=True, null=True)
    acctstopdelay = models.IntegerField(blank=True, null=True)
    xascendsessionsvrkey = models.CharField(max_length=20, blank=True, null=True)
    operator_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'radacct'


class Radcheck(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radcheck'


class Radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)
    comment = models.CharField(max_length=253)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radgroupcheck'


class Radgroupreply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)
    comment = models.CharField(max_length=253)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radgroupreply'


class Radippool(models.Model):
    pool_name = models.CharField(max_length=30)
    framedipaddress = models.CharField(max_length=15)
    nasipaddress = models.CharField(max_length=15)
    calledstationid = models.CharField(max_length=30)
    callingstationid = models.CharField(max_length=30)
    expiry_time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=64)
    pool_key = models.CharField(max_length=30)
    nasidentifier = models.CharField(max_length=64)
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    active = models.IntegerField()
    permanent_user_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radippool'


class Radpostauth(models.Model):
    username = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32)
    nasname = models.CharField(max_length=128)
    authdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radpostauth'


class Radreply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radreply'


class Radusergroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radusergroup'


class RealmMacUsers(models.Model):
    realm_id = models.IntegerField()
    mac = models.CharField(max_length=17, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'realm_mac_users'
        unique_together = (('realm_id', 'mac'),)


class RealmPmks(models.Model):
    realm_id = models.IntegerField()
    realm_ssid_id = models.IntegerField()
    ppsk = models.CharField(max_length=100, blank=True, null=True)
    pmk = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'realm_pmks'


class RealmSsids(models.Model):
    realm_id = models.IntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    ssid_type = models.CharField(max_length=10, blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    mesh_entry_id = models.IntegerField(blank=True, null=True)
    ap_profile_id = models.IntegerField(blank=True, null=True)
    ap_profile_entry_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'realm_ssids'


class RealmVlans(models.Model):
    realm_id = models.IntegerField()
    vlan = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'realm_vlans'


class Realms(models.Model):
    name = models.CharField(max_length=64)
    icon_file_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=14)
    cell = models.CharField(max_length=14)
    email = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    street_no = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    town_suburb = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    google_plus = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    t_c_title = models.CharField(max_length=255)
    t_c_content = models.TextField()
    suffix = models.CharField(max_length=200)
    suffix_permanent_users = models.IntegerField()
    suffix_vouchers = models.IntegerField()
    suffix_devices = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'realms'


class RegistrationRequests(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    registration_code = models.CharField(max_length=36, blank=True, null=True)
    state = models.CharField(max_length=22, blank=True, null=True)
    expire = models.DateTimeField(blank=True, null=True)
    email_sent = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=36, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration_requests'


class ReverseLookups(models.Model):
    ip = models.CharField(max_length=255)
    fqdn = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reverse_lookups'


class RollingLastDay(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_day'


class RollingLastHour(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_hour'


class RollingLastNinetyDays(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_ninety_days'


class RollingLastSevenDays(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_seven_days'


class RollingLastSixtyDays(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_sixty_days'


class RollingLastThirtyDays(models.Model):
    mesh_id = models.IntegerField(primary_key=True)
    tree_tag_id = models.IntegerField(blank=True, null=True)
    mesh_name = models.CharField(max_length=255, blank=True, null=True)
    tot_clients = models.BigIntegerField(blank=True, null=True)
    tot_tx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_rx_bytes = models.BigIntegerField(blank=True, null=True)
    tot_bytes = models.BigIntegerField(blank=True, null=True)
    tot_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes = models.BigIntegerField(blank=True, null=True)
    tot_lv_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_down = models.BigIntegerField(blank=True, null=True)
    tot_nodes_up = models.BigIntegerField(blank=True, null=True)
    dual_radios = models.BigIntegerField(blank=True, null=True)
    single_radios = models.BigIntegerField(blank=True, null=True)
    nup_beg_remove_secs = models.FloatField(blank=True, null=True)
    nup_end_add_secs = models.FloatField(blank=True, null=True)
    nup_up_seconds = models.FloatField(blank=True, null=True)
    nup_down_seconds = models.FloatField(blank=True, null=True)
    ndwn_beg_remove_secs = models.FloatField(blank=True, null=True)
    ndwn_end_add_secs = models.FloatField(blank=True, null=True)
    ndwn_up_seconds = models.FloatField(blank=True, null=True)
    ndwn_down_seconds = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolling_last_thirty_days'


class ScheduleEntries(models.Model):
    schedule_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=18, blank=True, null=True)
    command = models.CharField(max_length=255)
    predefined_command_id = models.IntegerField(blank=True, null=True)
    mo = models.IntegerField()
    tu = models.IntegerField()
    we = models.IntegerField()
    th = models.IntegerField()
    fr = models.IntegerField()
    sa = models.IntegerField()
    su = models.IntegerField()
    event_time = models.CharField(max_length=10)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schedule_entries'


class Schedules(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schedules'


class Sites(models.Model):
    name = models.CharField(max_length=64)
    cloud_id = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sites'


class SmsHistories(models.Model):
    cloud_id = models.IntegerField()
    recipient = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=25, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    reply = models.CharField(max_length=255, blank=True, null=True)
    sms_provider = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_histories'


class SocialLoginUserRealms(models.Model):
    social_login_user_id = models.IntegerField(blank=True, null=True)
    realm_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_login_user_realms'


class SocialLoginUsers(models.Model):
    provider = models.CharField(max_length=8, blank=True, null=True)
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    locale = models.CharField(max_length=5)
    timezone = models.IntegerField()
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    last_connect_time = models.DateTimeField(blank=True, null=True)
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_login_users'


class Softflows(models.Model):
    dynamic_client_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    src_mac = models.CharField(max_length=64, blank=True, null=True)
    src_ip = models.CharField(max_length=64, blank=True, null=True)
    dst_ip = models.CharField(max_length=64, blank=True, null=True)
    src_port = models.IntegerField(blank=True, null=True)
    dst_port = models.IntegerField(blank=True, null=True)
    proto = models.IntegerField(blank=True, null=True)
    pckt_in = models.IntegerField(blank=True, null=True)
    pckt_out = models.IntegerField(blank=True, null=True)
    oct_in = models.BigIntegerField(blank=True, null=True)
    oct_out = models.BigIntegerField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'softflows'


class TempFlowLogs(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    ap_id = models.IntegerField(blank=True, null=True)
    ap_profile_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255)
    proto = models.IntegerField()
    src_mac = models.CharField(max_length=255)
    src_ip = models.CharField(max_length=255)
    src_port = models.IntegerField()
    dst_ip = models.CharField(max_length=255)
    dst_port = models.IntegerField()
    oct_in = models.IntegerField()
    pckt_in = models.IntegerField()
    oct_out = models.IntegerField()
    pckt_out = models.IntegerField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_flow_logs'


class TempProxyLogs(models.Model):
    node_id = models.IntegerField(blank=True, null=True)
    mesh_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    source_ip = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    full_string = models.TextField(blank=True, null=True)
    full_url = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_proxy_logs'


class TempReports(models.Model):
    mesh_id = models.IntegerField()
    node_id = models.IntegerField()
    ap_id = models.IntegerField()
    ap_profile_id = models.IntegerField()
    report = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temp_reports'


class Timezones(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'timezones'


class TopUpTransactions(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    permanent_user_id = models.IntegerField(blank=True, null=True)
    permanent_user = models.CharField(max_length=255, blank=True, null=True)
    top_up_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    action = models.CharField(max_length=6, blank=True, null=True)
    radius_attribute = models.CharField(max_length=30)
    old_value = models.CharField(max_length=30, blank=True, null=True)
    new_value = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'top_up_transactions'


class TopUps(models.Model):
    cloud_id = models.IntegerField(blank=True, null=True)
    permanent_user_id = models.IntegerField(blank=True, null=True)
    data = models.BigIntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    days_to_use = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    type = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'top_ups'


class UnknownDynamicClients(models.Model):
    nasidentifier = models.CharField(unique=True, max_length=128)
    calledstationid = models.CharField(unique=True, max_length=128)
    last_contact = models.DateTimeField(blank=True, null=True)
    last_contact_ip = models.CharField(max_length=128)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'unknown_dynamic_clients'


class UnknownNodes(models.Model):
    mac = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    from_ip = models.CharField(max_length=15)
    gateway = models.IntegerField()
    last_contact = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    new_server = models.CharField(max_length=255)
    new_server_status = models.CharField(max_length=8, blank=True, null=True)
    name = models.CharField(max_length=255)
    firmware_key_id = models.IntegerField(blank=True, null=True)
    new_server_protocol = models.CharField(max_length=5, blank=True, null=True)
    new_mode = models.CharField(max_length=4, blank=True, null=True)
    new_mode_status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unknown_nodes'


class UserSettings(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_settings'


class UserSsids(models.Model):
    username = models.CharField(max_length=64)
    ssidname = models.CharField(max_length=64)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_ssids'


class UserStats(models.Model):
    radacct_id = models.IntegerField()
    username = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.CharField(max_length=15)
    nasidentifier = models.CharField(max_length=64)
    framedipaddress = models.CharField(max_length=15)
    callingstationid = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    acctinputoctets = models.BigIntegerField()
    acctoutputoctets = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_stats'


class UserStatsDailies(models.Model):
    user_stat_id = models.IntegerField()
    username = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasidentifier = models.CharField(max_length=64)
    callingstationid = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    acctinputoctets = models.BigIntegerField()
    acctoutputoctets = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_stats_dailies'


class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    token = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    active = models.IntegerField()
    country_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    timezone_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vouchers(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    batch = models.CharField(max_length=128)
    status = models.CharField(max_length=8, blank=True, null=True)
    perc_time_used = models.IntegerField(blank=True, null=True)
    perc_data_used = models.IntegerField(blank=True, null=True)
    last_accept_time = models.DateTimeField(blank=True, null=True)
    last_reject_time = models.DateTimeField(blank=True, null=True)
    last_accept_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_nas = models.CharField(max_length=128, blank=True, null=True)
    last_reject_message = models.CharField(max_length=255, blank=True, null=True)
    cloud_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    extra_name = models.CharField(max_length=100)
    extra_value = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    realm = models.CharField(max_length=50)
    realm_id = models.IntegerField(blank=True, null=True)
    profile = models.CharField(max_length=50)
    profile_id = models.IntegerField(blank=True, null=True)
    expire = models.DateTimeField(blank=True, null=True)
    time_valid = models.CharField(max_length=10)
    data_used = models.BigIntegerField(blank=True, null=True)
    data_cap = models.BigIntegerField(blank=True, null=True)
    time_used = models.IntegerField(blank=True, null=True)
    time_cap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vouchers'
