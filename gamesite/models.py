# models.py
from django.db import models

class Card(models.Model):
    image = models.ImageField(upload_to='memorygame/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def image_url(self):
        return self.image.url
class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    image_url = models.ImageField(upload_to='images/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url