from django.contrib import admin
from django.utils.html import format_html
from .models import Image, Card, CardCategory

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image_thumbnail','name', 'is_premium')
    search_fields = ('is_premium',)

    def image_thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url.url)
        return "No Image"

    image_thumbnail.short_description = 'Image Preview'


@admin.register(CardCategory)
class CardCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CardAdmin(admin.ModelAdmin):
    list_display = ('category','card_thumbnail','name', 'is_premium')
    search_fields = ('is_premium','category',)
    list_filter = ('category', 'is_premium')  # Add category filter here
    def card_thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url.url)
        return "No Image"

    card_thumbnail.short_description = 'Card Preview'

# Register your models with the admin site
admin.site.register(Image, ImageAdmin)
admin.site.register(Card, CardAdmin)
