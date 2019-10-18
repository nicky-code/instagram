from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'likes','user','profile','comments']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        