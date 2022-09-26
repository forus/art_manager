from rest_framework import viewsets
from inventory.models import ArtItem
from inventory.api.serializers import ArtItemSerializer

class ArtItemViewSet(viewsets.ModelViewSet):
    queryset = ArtItem.objects.all()
    serializer_class = ArtItemSerializer