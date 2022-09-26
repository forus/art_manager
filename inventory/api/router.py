from .viewsets import *
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'spots', SpotViewSet)
router.register(r'art-items', ArtItemViewSet)
router.register(r'art-locations', ArtLocationViewSet)
router.register(r'art-borrowing-request', ArtBorrowingRequestViewSet)