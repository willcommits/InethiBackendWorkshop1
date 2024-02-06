# permissions.py

from rest_framework.permissions import BasePermission
from jose import jwt, JWTError
from django.conf import settings


class IsAdminUser(BasePermission):
    message = "Access denied. User must be an admin."

    def has_permission(self, request, view):
        # Extract the token from the Authorization header
        auth = request.headers.get('Authorization', None)
        print(auth)
        if auth:
            token = auth.split()[1]

            try:
                # Decode the token
                key = settings.KEYCLOAK_PUBLIC_KEY  # You need to add your Keycloak public key in settings
                decoded_token = jwt.decode(token, key, algorithms=['RS256'], audience='manage-backend')

                # Check if the admin role is present in the token
                roles = decoded_token.get('realm_access', {}).get('roles', [])

                print(roles)
                if 'admin' in roles:
                    return True
            except jwt.JWTError as e:
                print(e)
                pass
        return False
