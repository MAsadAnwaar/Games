from django.db import models
import os
class Image(models.Model):
    name = models.CharField(max_length=10)
    image_url = models.ImageField(upload_to='apiimages/')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url


def get_card_image_upload_path(instance, filename):
    category_name = instance.category.name
    category_name = category_name.replace(" ", "_")
    return os.path.join('apicard', category_name, filename)

class CardCategory(models.Model):
    name = models.CharField(max_length=50, default="Food")

    def __str__(self):
        return self.name

class Card(models.Model):
    category = models.ForeignKey(CardCategory, on_delete=models.CASCADE, related_name='cards')
    name = models.CharField(max_length=10)
    image_url = models.ImageField(upload_to=get_card_image_upload_path)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.image_url.url

    @classmethod
    def get_next_card_name(cls, category):
        # Get all cards in the category and determine the highest number
        cards = cls.objects.filter(category=category)
        if cards:
            max_number = max(int(card.name) for card in cards if card.name.isdigit())
        else:
            max_number = 0
        return str(max_number + 1)

    def save(self, *args, **kwargs):
        if not self.pk and not self.name:
            self.name = self.get_next_card_name(self.category)
        super().save(*args, **kwargs)