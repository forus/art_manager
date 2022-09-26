from rest_framework import serializers
from inventory.models import ArtItem

class ArtItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtItem
        fields = '__all__'