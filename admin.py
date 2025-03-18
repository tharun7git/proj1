from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Folder, Photo

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'category', 'uploaded_at')
    search_fields = ('title', 'folder__name', 'category')
    list_filter = ('folder', 'category')
