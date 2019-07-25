from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .models import ImageField
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField('Profile',related_name='followers_profile',blank=True)
    following = models.ManyToManyField('Profile',related_name='following_profile',blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',format='JPEG',options={'quality':100},null=True,blank=True)
    bio = models.CharField(max_length=200,null=True,blank=True)

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def search_user(cls,username):
        searched_user = User.objects.get(username = username)
        return searched_user

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image_title = models.CharField(max_length = 100)
    image_caption = HTMLField()
    image = models.ImageField(upload_to = 'posts',format='JPEG',options={'quality':100})
    user_profile = models.ForeignKey(User,null=True,blank=True,on_delete = models.CASCADE)
    posted_on = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)

    def get_number_of_comments(self):
        return self.comment_set.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_image(cls,image_id):
        image = cls.objects.get(id=image_id)

    def update_caption(self,caption):
        self.image_caption = caption
        self.save()

    def __str__(self):
        return self.image_title


class Comment(models.Model):
    post = models.ForeignKey('Image',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment
