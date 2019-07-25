from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to="ProfilePicture/")
    date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        Profile.objects.filter(id =self.pk).delete()
        
    def update_profile(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
class Image(models.Model):
    image =models.ImageField(upload_to = 'pics/',null=True)
    name = models.CharField(ma_length=50)
    caption=models.CharField(max_length =1000)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank=True)
    likes=models.ManyToManyField('Profile',default=False,blank=True,related_name='likes')
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        image.objects.filter(id =self.pk).delete()
        
    def update_caption(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)