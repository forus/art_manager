from django.db import models

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

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.email})"

class ArtItem(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    creation_date = models.DateField()

    def __str__(self):
        return f"{self.name} (by {self.author})"

class ArtLocation(models.Model):
    class Meta:
        unique_together = (('art_item', 'spot'),)
    art_item = models.OneToOneField(ArtItem, primary_key=True, on_delete=models.PROTECT) 
    spot = models.ForeignKey(Spot, on_delete=models.PROTECT) 
    responsible_person = models.ForeignKey(Person, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.art_item} at {self.spot}"
