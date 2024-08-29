from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=10)
    image_url = models.ImageField(upload_to='apiimages/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url

class Card(models.Model):
    name = models.CharField(max_length=10)
    image_url = models.ImageField(upload_to='apicard/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url