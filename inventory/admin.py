from django.contrib import admin

from .models import Building, Spot, Person, ArtItem, ArtLocation 

admin.site.register(Building)
admin.site.register(Spot)
admin.site.register(Person)
admin.site.register(ArtItem)
admin.site.register(ArtLocation)
