from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile,Image,Comment

class PostImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image_title','image','image_caption',)


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)