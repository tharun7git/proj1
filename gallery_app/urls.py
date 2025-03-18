

from django.urls import path, include
from django.contrib import admin
from gallery_app.views import home,camera_photos
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home),
    path('camera/', camera_photos,name='camera'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
