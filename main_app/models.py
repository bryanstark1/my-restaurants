from django.db import models
from django.urls import reverse

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})