from django.test import TestCase
from .models import Comment,Image,Profile
import datetime as dt
# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):

        # Creating a new tag and saving it
        self.new_image = Image(name = 'testing')
        self.new_image.save()

        self.new_profile= Profile(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_profile.save()

        self.new_image.profile.add(self.new_profile)

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()