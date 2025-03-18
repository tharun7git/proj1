from django.shortcuts import render
from .models import Photo

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def others(request):
    return render(request, 'others.html')

from .models import Photo

def camera_photos(request):
    photos = Photo.objects.filter(category="Camera")  # Fetch only Camera images
    return render(request, 'camera.html', {'photos': photos})
