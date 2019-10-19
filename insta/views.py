from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,ProfileForm
from .models import Image,Profile,Comment,Follow
import datetime as dt

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    
   image=Image.objects.all()
   current_user = request.user
   myProfile = Profile.objects.filter(user = current_user).first()
   print(image)
   return render(request, 'welcome.html',{"image":image,"myProfile":myProfile})

@login_required(login_url='/accounts/login/')
def new_image(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = ImageForm()
    
    return render(request, 'new_image.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    
    current_user = request.user
    profil = Profile.objects.filter(id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
        return redirect('myProfile')

    else:
        form = ProfileForm()
    
    return render(request, 'new-profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def myProfile(request):
    
   current_user = request.user 
   all_images = Image.objects.filter(user=current_user)
   myProfile = Profile.objects.filter(user = current_user).first()
   return render(request, 'profile.html', {"all_images":all_images, "myProfile":myProfile})


@login_required(login_url='/accounts/login/')
def search_users(request):
    
   if 'username' in request.GET and request.GET["username"]:
       search_term = request.GET.get("username")
       searched_users = Profile.search_by_profile(search_term)
       print(searched_users)
       message = f"{search_term}"
       return render(request, "all-instagram/search.html",{"message":message,"users": searched_users})
   else:
       message = "You haven't searched for any term"
       return render(request, 'all-instagram/search.html',{"message":message})

