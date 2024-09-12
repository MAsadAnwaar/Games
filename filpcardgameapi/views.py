from rest_framework import generics
from .models import Image, Card, CardCategory
from .serializers import ImageSerializer, CardSerializer
from rest_framework.response import Response

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CardListView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class categorycardimages(generics.ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        # Return all cards for this view, but we'll handle grouping in the response
        return Card.objects.all()

    def list(self, request, *args, **kwargs):
        # Fetch all categories with their associated cards
        categories = CardCategory.objects.prefetch_related('cards').all()

        # Construct the response data
        response_data = []
        for category in categories:
            category_data = {
                'category': category.name,
                'cards': CardSerializer(category.cards.all(), many=True, context={'request': request}).data
            }
            response_data.append(category_data)

        return Response(response_data)


from django.shortcuts import render, redirect
from .forms import CardUploadForm
from django.contrib import messages
from .models import Card
import os
def upload_cards(request):
    if request.method == 'POST':
        form = CardUploadForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            images = request.FILES.getlist('images')
            try:
                for image in images:
                    card = Card(category=category, image_url=image)
                    card.name = Card.get_next_card_name(category)
                    card.save()
                messages.success(request, 'Images uploaded successfully!')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
            return redirect('upload_cards')  # Redirect to the same page to show messages
    else:
        form = CardUploadForm()
    
    return render(request, 'upload_cards.html', {'form': form})

    
import requests
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.contrib import messages
from .models import Image
from .forms import URLForm

def download_images_from_urls(urls):
    messages_list = []
    for index, url in enumerate(urls, start=1):
        try:
            response = requests.get(url.strip())
            response.raise_for_status()

            image_name = str(index)
            image_content = ContentFile(response.content, f'{image_name}.jpg')

            image_instance = Image(name=image_name, image_url=image_content)
            image_instance.save()
            messages_list.append(f'Successfully downloaded image from {url}.')
        except requests.RequestException as e:
            messages_list.append(f'Failed to download image from {url}. Error: {e}')
        except Exception as e:
            messages_list.append(f'Failed to save image {image_name}. Error: {e}')
    return messages_list

def image_upload_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            urls = form.cleaned_data['urls'].split('\n')
            messages_list = download_images_from_urls(urls)
            for message in messages_list:
                messages.info(request, message)  # Use messages.info for non-error/success messages
            return redirect('image_upload')  # Redirect after POST
    else:
        form = URLForm()
    return render(request, 'image_upload.html', {'form': form})

