from rest_framework import viewsets
from inventory.models import Spot
from inventory.api.serializers import SpotSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer