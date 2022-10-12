from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from .views import (InventoryViewSet)
# from .views import (InventoryViewSet)
from . import views

router = routers.DefaultRouter()
router.register(r'api/inventory', views.InventoryViewSet)


urlpatterns = [
    path("inventoryy", views.index),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
