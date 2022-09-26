from rest_framework import serializers
from inventory.models import ArtBorrowingRequest

class ArtBorrowingRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtBorrowingRequest
        fields = '__all__'