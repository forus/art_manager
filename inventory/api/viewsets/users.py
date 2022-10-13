from rest_framework import viewsets
from django.contrib.auth.models import User
from inventory.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Enpoint to create/read/update/delete a user enity
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Enpoint to create a user enity
        """
        super().create(request, *args, **kwargs)