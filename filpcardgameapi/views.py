from rest_framework import generics
from .models import Image, Card
from .serializers import ImageSerializer, CardSerializer

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CardListView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer