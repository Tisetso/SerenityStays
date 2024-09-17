from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='properties/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"Booking for {self.property.title} by {self.name}"
