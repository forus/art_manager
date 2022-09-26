from rest_framework import serializers
from inventory.models import Building

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ['address']