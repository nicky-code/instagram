from django import forms
from .models import Image,Profile,Comments


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
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user_profile','image_comment']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class InstagramForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
         