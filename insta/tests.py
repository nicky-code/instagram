from django.test import TestCase
from .models import Image,Profile,Comments
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    a class to test the profile instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='nicky')
        self.profile= Profile(profile_photo='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg',bio='nice',user=self.user)
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    #Testing the save method
    '''
    function to check the save method of image
    '''
    
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>=1)
        
    #Testing the delete method
    def test_delete_method(self):
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_photo='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg').first()
        delete= Profile.objects.filter(profile_photo=profil.profile_photo).delete()
        profile=Profile.objects.all()
        self.assertFalse(len(profile)==1)
         