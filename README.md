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

If you're running the backend for the first time, you will have to migrate changes to the database with
```bash
python manage.py migrate
```
You may also want to create an admin user with the `createsuperuser` django command.

Now you can run the server, using
```bash
python manage.py runserver
```

## External services

The management backend uses some 'external' services for authentication and monitoring, namely [Prometheus]('https://prometheus.io/') and [Keycloak]('https://www.keycloak.org/'). For development, we can host these services locally and point the backend to their local URLs.

### Keycloak

Follow the instructions at https://www.keycloak.org/getting-started/getting-started-docker for getting a local keycloak server up and running in a Docker container. Call the new realm you create 'inethi-global-services' and add an admin user. Assign this user a new role, called 'admin' - this is crucial for authentication with the backend.

Once you have a keycloak server running, navigate to `Realm Settings > Keys` and copy the RS256 public key. Add it to a file called 'keycloak.cert', at the root directory.

### Prometheus

TODO
