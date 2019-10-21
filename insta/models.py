from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to ='photos/',null=True)
    bio = models.CharField(max_length=35,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio
    
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @classmethod    
    def update_profile(self):
        self.update()
        
    @classmethod
    def search_by_profile(cls,username):
       certain_user = cls.objects.filter(user__username__icontains=username)
       
       return  certain_user
   
    @classmethod
    def get_by_id(cls,id):
        profile=Profile.objects.get(user=id)
     
        return profile

class Image(models.Model):
    image = models.ImageField(upload_to ='images/',null=True)
    image_name = models.CharField(max_length=35)
    image_caption=models.CharField(max_length=35,null=True)
    profile=models.ForeignKey(Profile,null=True)
    posted_time = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
    
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    def update_caption(self):
        caption=self.image_caption.update()
        return caption
    
    @classmethod
    def get_all_images(cls):
        images =cls.objects.all().prefetch_related('comments_set')
        return images

    
    @classmethod
    def get_profile_picture(cls,profile):
        images = Image.objects.filter(profile_photo=profile)
        return images
    
    def display_images(cls):
        images=cls.objects.all()
        return images
    
        

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    image_comment = models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.comment
    
    
    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()
        
    def update_comment(self):
        self.update()
        
        
class Follow(models.Model):
    profile = models.ForeignKey(Profile,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile 
    
    
class InstagramWelcomeRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
        