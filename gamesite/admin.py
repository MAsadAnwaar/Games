from django.contrib import admin
from django.utils.html import format_html
from .models import Card, BackgroundImage

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')  # Updated to use image_preview method
    search_fields = ('name',)  # Fields to search within
    list_filter = ('name',)  # Fields to filter by

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'No Image'
    
    image_preview.short_description = 'Image Preview'

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview')  # Updated to use image_preview method
    search_fields = ('name',)  # Fields to search within
    list_filter = ('name',)  # Fields to filter by

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'No Image'
    
    image_preview.short_description = 'Image Preview'
