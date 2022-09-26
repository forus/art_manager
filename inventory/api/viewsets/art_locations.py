from rest_framework import viewsets
from inventory.models import ArtLocation
from inventory.api.serializers import ArtLocationSerializer

class ArtLocationViewSet(viewsets.ModelViewSet):
    queryset = ArtLocation.objects.all()
    serializer_class = ArtLocationSerializer