from django import forms
from .models import Card

class CardUploadForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = Card
        fields = ['category', 'images']
