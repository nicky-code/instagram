from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    
   image=Image.objects.all()
   print(image)
   return render(request, 'welcome.html',{"image":image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    
    # image=Image.objects.all()
    
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
    
    return render(request, 'welcome.html',{"form":form})
