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
    function to check the save method of profile
    '''
    
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>=1)
        
    #Testing the delete method
    def test_delete_method(self):
        '''
        function to check the delete method of profile
        '''
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_photo='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg').first()
        delete= Profile.objects.filter(profile_photo=profil.profile_photo).delete()
        profile=Profile.objects.all()
        self.assertFalse(len(profile)==1)

    #Testing the update method
    def test_update_profile(self):
        '''
        a method that helps to update the profile
        
        ''' 
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_photo='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg').first()
        update = Profile.objects.filter(profile_photo=profil.profile_photo).update(profile_photo='pic')
        updated = Profile.objects.filter(profile_photo='pic').first()
        self.assertNotEqual(profil.profile_photo,updated.profile_photo)
        
        
class ImageTestClass(TestCase):
    '''
    a class to test the image instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='nicky')
        self.image= Image(image='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg',image_name='nicole',image_caption='lovely',posted_time='2pm',likes='1',user=self.user)
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    #Testing the save method
    '''
    function to check the save method of image
    '''
    
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>=1)
        
    #Testing the delete method
    def test_delete_method(self):
        self.image.save_image()
        images= Image.objects.filter(image='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg').first()
        delete= Image.objects.filter(image=images.image).delete()
        image=Image.objects.all()
        self.assertFalse(len(image)==1)

    #Testing the update method
    def test_update_image(self):
        '''
        a method that helps to update the image
        
        ''' 
        self.image.save_image()
        images= Image.objects.filter(image='/home/nicky/Downloads/IMG-20181015-WA0007-1.jpg').first()
        update = Image.objects.filter(image=images.image).update(image='photos')
        updated = Image.objects.filter(image='photos').first()
        self.assertNotEqual(images.image,updated.image)
            
            
class CommentsTestClass(TestCase):
    '''
    a class to test the comments instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='nicky')
        self.comments = Comments.objects.create(comment = 'wow')
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comments,Comments))
        
    #Testing the save method
    '''
    function to check the save method of comments
    '''
    
    def test_save_method(self):
        self.comments.save_comment()
        comment = Comments.objects.all()
        self.assertTrue(len(comment)>=1)
        
    #Testing the delete method
    def test_delete_method(self):
        
        self.comments.save_comment()
        self.comments.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) >= 0)


    #Testing the update method
    def test_update_comment(self):
        '''
        a method that helps to update the comment
        
        ''' 
        self.comments.save_comment()
        commented= Comments.objects.filter(comment='wow').first()
        update = Comments.objects.filter(comment=commented.comment).update(comment='lovely')
        updated = Comments.objects.filter(comment='lovely').first()
        self.assertNotEqual(commented.comment,updated.comment)
            
            