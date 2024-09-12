from django import forms
from .models import Card

class CardUploadForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = Card
        fields = ['category', 'images']

from django import forms

class URLForm(forms.Form):
    urls = forms.CharField(widget=forms.Textarea, help_text="Enter image URLs, each on a new line.")
