from django.contrib import admin

from .models import ArtBorrowingRequest, Building, Spot, ArtItem, ArtLocation

admin.site.register(Building)
admin.site.register(Spot)
admin.site.register(ArtItem)
admin.site.register(ArtLocation)
admin.site.register(ArtBorrowingRequest)