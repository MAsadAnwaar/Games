from django.db import models

class Image(models.Model):
    image_url = models.ImageField(upload_to='images/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url
        
class Card(models.Model):
    image_url = models.ImageField(upload_to='card/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url