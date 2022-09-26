from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

class Spot(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.CharField(max_length=50)
    floor = models.IntegerField(default=0)
    details = models.CharField(max_length=500)

    def __str__(self):
        return f"${self.building}, {self.room} room, {self.floor} floor"

class ArtItem(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    creation_date = models.DateField()
    photo = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name} (by {self.author})"

class ArtLocation(models.Model):
    """
    Shows that an art work is/were placed in a certain spot
    """
    art_item = models.ForeignKey(ArtItem, on_delete=models.PROTECT)
    spot = models.ForeignKey(Spot, on_delete=models.PROTECT) 
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    responsible_person = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.art_item} at {self.spot}"