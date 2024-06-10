from django.contrib import admin
from django.db.models import Model
from . import models

# Register all radiusdesk models
for (name, cls) in models.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, Model):
        admin.site.register(cls)
