from django.urls import path
from .views import ImageListView, CardListView, categorycardimages, image_upload_view
from . import views

urlpatterns = [
    path('backgroundimages/', ImageListView.as_view(), name='image-list'),
    path('cardimages/', CardListView.as_view(), name='card-list'),
    path('categorycardimages/', categorycardimages.as_view(), name='categorycardimages'),
    path('upload-cards/', views.upload_cards, name='upload_cards'),
    path('upload-images/', image_upload_view, name='image_upload'),
]
