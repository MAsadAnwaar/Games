# admin.py
from django.contrib import admin
from .models import Card, BackgroundImage

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to search within
    list_filter = ('name',)  # Fields to filter by

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to search within
    list_filter = ('name',)  # Fields to filter by
