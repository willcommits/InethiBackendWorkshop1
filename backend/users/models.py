from django.db import models

# Create your models here.
class User(models.Model):
    keycloak_username = models.CharField(max_length=50, unique=True)
    wallet_address = models.CharField(max_length=50)
