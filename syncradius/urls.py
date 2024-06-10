from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("meshes", views.MeshViewSet)
router.register("nodes", views.NodeViewSet)
router.register("aps", views.ApViewSet)

urlpatterns = [path("", include(router.urls))]
