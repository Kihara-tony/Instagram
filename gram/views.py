from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
from . import PostImageForm,ProfileEditForm,CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import datetime
from django.template.loader import render_to_string
# from email import send_welcome_email

# Create your views here.
@login_required(login_url="/accounts/login")
def account(request,username):
    user = User.objects.get(username = username )
    profile = Profile.objects.filter(user = user).first()
    images = Image.objects.filter(user_profile = profile.user).all()
    return render(request,'account.html',{'profile':profile,'images':images})
def image(request,image_id):
    image = Image.objects.get(id = image_id)
    poster = Profile.objects.get(user=image.user_profile)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            user = request.user
            comment = Comment(user=request.user,post=image,comment=request.POST['comment'])
            comment.save()
            return redirect(reverse('singleImage',args=[image.id]))
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post = image.id).all()
    return render(request,'image.html',{'is_liked':is_liked,'comments':comments,'image':image,'form':form,'poster':poster})

def search(request):
    try:
        if 'profile' in request.GET and request.GET['profile']:
            search_term = request.GET.get('profile')
            searched_profile = User.objects.get(username__icontains = search_term)
            profile = Profile.objects.filter(user = searched_profile).first()
            images = Image.objects.filter(user_profile = searched_profile).all()
            return render(request,'account.html',{'profile':profile,'images':images})
    except (ValueError,User.DoesNotExist):
        raise Http404()

    return render(request,'account.html',{'profile':profile,'images':images})
def signout(request):
    logout(request)
    return redirect('account')
@login_required
def profile_edit(request,username):
    user = User.objects.get(username=username)
    if request.user != user:
        return redirect('index')

    if request.method == 'POST':
        form = ProfileEditForm(request.POST,instance=user.profile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('account',kwargs={'username':user.username}))

    else:
        form = ProfileEditForm(instance=user.profile)

    context = {
        'user':user,
        'form':form
    }
    return render(request,'profile_edit.html',context)
def post_picture(request):
    if request.method == 'POST':
        form = PostImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            post = Image(user_profile=request.user,image_title=request.POST['image_title'],image=request.FILES['image'],image_caption=request.POST['image_caption'],posted_on=datetime.datetime.now())
            post.save()
            return redirect(reverse('account',kwargs={'username':request.user.username}))
    else:
        form = PostImageForm()
    return render(request,'post_pic.html',{'form':form})
