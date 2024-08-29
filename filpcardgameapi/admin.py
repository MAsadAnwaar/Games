from django.contrib import admin
from django.utils.html import format_html
from .models import Image, Card

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'is_premium')
    search_fields = ('is_premium',)

    def image_thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url.url)
        return "No Image"

    image_thumbnail.short_description = 'Image Preview'

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_thumbnail', 'is_premium')
    search_fields = ('is_premium',)

    def card_thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url.url)
        return "No Image"

    card_thumbnail.short_description = 'Card Preview'

# Register your models with the admin site
admin.site.register(Image, ImageAdmin)
admin.site.register(Card, CardAdmin)
