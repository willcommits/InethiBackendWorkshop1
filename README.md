# API for iNethi Management Backend

## Installation

Set up a virtual environment with by running
```bash
python -m venv .venv
```
from the command line. Now you can activate it with
```bash
source .venv/bin/activate
```
Next, install the dependencies (Django, Jose etc)
```bash
pip install -r requirements.txt
```

### External services

The management backend uses some 'external' services for config, authentication and monitoring, namely [RadiusDesk]('https://www.radiusdesk.com/'), [Keycloak]('https://www.keycloak.org/') and [Prometheus]('https://prometheus.io/'). For development, we can host these services locally and point the backend to their local URLs. These need to be setup and running first before running the backend.

#### Keycloak

Keycloak manages user authorisation and authentication on both the backend and frontend.

Follow the instructions at https://www.keycloak.org/getting-started/getting-started-docker for getting a local keycloak server up and running in a Docker container. Call the new realm you create 'inethi-global-services' and add an admin user. Assign this user a new role, called 'admin' - this is crucial for authentication with the backend.

#### Radiusdesk

The CommuNethi app is designed to run alongside a RadiusDesk server. It provides some existing functionality in a new UI as well as extended functionality. To avoid syncing errors, it connects to the same mysql database that is used by radiusdesk, which needs some extra configuration:

First follow the [instructions for running radiusdesk in a docker container]('https://www.radiusdesk.com/wiki24/install_docker'). Then make sure that the mariadb container exposes its database at port 3306, so that django can connect to it. This may involve editing radiusdesk's `docker-compose.yml` file.

Double check the database is exposed by running
```bash
mysql -h localhost -P 3306 -u rd --password=rd
```

#### Prometheus (TODO)

## Running the backend

If you're running the backend for the first time, you will have to migrate changes to the database with
```bash
python manage.py migrate
```
You may also want to create an admin user with the `createsuperuser` django command.

Now you can run the server, using
```bash
python manage.py runserver
```

The base url should redirect you to the keycloak server, where you can log in using the credentials you set up initially. After that, you should be able to access the admin site.
