from rest_framework import viewsets
from inventory.models import ArtBorrowingRequest
from inventory.api.serializers import ArtBorrowingRequestSerializer

class ArtBorrowingRequestViewSet(viewsets.ModelViewSet):
    queryset = ArtBorrowingRequest.objects.all()
    serializer_class = ArtBorrowingRequestSerializer