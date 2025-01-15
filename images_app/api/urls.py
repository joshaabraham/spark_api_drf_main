from django.urls import path
from images_app.api.views import AlbumListCreateView, AlbumPhotosListView, AlbumRetrieveUpdateDestroyView, PhotoListCreateView, PhotoRetrieveUpdateDestroyView, UploadImageView



urlpatterns = [
    
    path('upload-profile-image/', UploadImageView.as_view(), name='upload-profile-image'),
    
    # Routes pour Album
     path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<int:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail'),

    # Endpoints pour les photos
    path('photos/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-detail'),

    path('albums/<int:album_id>/photos/', AlbumPhotosListView.as_view(), name='album-photos-list'),
]