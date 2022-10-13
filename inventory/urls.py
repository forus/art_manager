import imp
from rest_framework.schemas import get_schema_view
from django.urls import include, path

from .api import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('openapi/', get_schema_view(
        title="Art Manager",
        description="API of Art Manager project",
        version="1.0.0"
    ), name='openapi-schema'),
]
