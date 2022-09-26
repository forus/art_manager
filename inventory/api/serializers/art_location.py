from rest_framework import serializers
from inventory.models import ArtLocation

class ArtLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtLocation
        fields = '__all__'