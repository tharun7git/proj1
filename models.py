from django.db import models

# Create your models here.
from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    FOLDER_CHOICES = [
        ('Camera', 'Camera'),
        ('Screenshots', 'Screenshots'),
        ('WhatsApp', 'WhatsApp'),
        ('Edits', 'Edits'),
        ('Downloads', 'Downloads'),
        ('Others', 'Others'),
    ]

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="photos")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=FOLDER_CHOICES)

    def save(self, *args, **kwargs):
        # Automatically assign the correct folder
        folder_obj, _ = Folder.objects.get_or_create(name=self.category)
        self.folder = folder_obj
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
