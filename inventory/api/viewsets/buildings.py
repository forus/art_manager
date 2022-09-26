from rest_framework import viewsets
from inventory.models import Building
from inventory.api.serializers import BuildingSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer