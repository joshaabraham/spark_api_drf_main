from django.db import models
from django.conf import settings
import os


def user_directory_path(instance, filename):
    return f'uploads/users/{instance}/{filename}'


class Album(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='albums')
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    sharing_settings = models.CharField(
        max_length=50, 
        choices=[('public', 'Public'), ('private', 'Private'), ('shared', 'Shared')],
        default='private'
    )
    is_archived = models.BooleanField(default=False)
    tags = models.TextField(blank=True, null=True)
    last_accessed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_photos(self):
        """Retourne toutes les photos associées à cet album."""
        return self.photos.all()

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    date_taken = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    camera_model = models.CharField(max_length=255, blank=True, null=True)
    camera_make = models.CharField(max_length=255, blank=True, null=True)
    camera_settings = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    likes_count = models.PositiveIntegerField(default=0)
    is_favorite = models.BooleanField(default=False)
    tags = models.TextField(blank=True, null=True)
    photographer = models.CharField(max_length=255, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    exif_data = models.TextField(blank=True, null=True)
    file_format = models.CharField(max_length=10, blank=True, null=True)
    file_size = models.PositiveBigIntegerField(blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    image_orientation = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Dynamically define the upload_to path based on the album
        if self.album and not self.image.name.startswith(f'albums/{self.album.id}/'):
            self.image.name = f'albums/{self.album.id}/{self.image.name}'
        super().save(*args, **kwargs)
