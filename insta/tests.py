from django.test import TestCase
from .models import UserImage,Location,Category

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
        
        