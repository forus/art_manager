from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.urls import include, path

from .api import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('openapi/', get_schema_view(
        title="Art Manager",
        description="API of Art Manager project",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
