import imp
from django.urls import include, path
from .api import router

urlpatterns = [
    path('api/', include(router.urls)),
]
