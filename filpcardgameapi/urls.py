from django.urls import path
from .views import ImageListView, CardListView

urlpatterns = [
    path('backgroundimages/', ImageListView.as_view(), name='image-list'),
    path('cardimages/', CardListView.as_view(), name='card-list'),
]
