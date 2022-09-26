from rest_framework import serializers
from inventory.models import Spot

class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = ['building', 'room', 'floor', 'details']