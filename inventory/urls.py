from django.urls import include, path

from inventory.viewsets import UserViewSet

from .models import Building, Spot
from rest_framework import routers, serializers, viewsets

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ['address']

class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = ['building', 'room', 'floor', 'details']

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

router = routers.DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'spots', SpotViewSet)

admin_router = routers.DefaultRouter()
admin_router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(admin_router.urls)),
]
