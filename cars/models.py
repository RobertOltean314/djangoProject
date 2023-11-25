from django.db import models


# Create your models here.

class Car(models.Model):
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    color = models.CharField(max_length=15)
    horse_power = models.IntegerField()
    technical_specifications = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'
