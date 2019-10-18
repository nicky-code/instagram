from django import forms
from .models import Image,Profile


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'likes','user','profile','comments']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile','user_id']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
        