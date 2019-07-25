from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Image,Profile
# from email import send_welcome_email

# Create your views here.
@login_required(login_url="/accounts/login")
def landing_page(request):
    return render(request,'index.html')
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input =request.GET.get('image')
        searched_images =Image.search_by_category(search_input)
        message = f"{search_input}"
        return render(request,'search.html',{"message":message,"images":searched_images})
    else:
        message = "Please input something in the search field"
        return render(request,"search.html",{"message":message})
def single_pic(request):
    image=Image.get_pic()
    return render(request, "singlepic.html",{"image":image})

