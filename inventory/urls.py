from django.urls import include, path

from inventory.viewsets import *
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'spots', SpotViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
