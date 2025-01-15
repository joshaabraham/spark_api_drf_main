from rest_framework import generics
from images_app.models import Album, Photo
from images_app.api.serializers import AlbumSerializer, PhotoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = PhotoSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Image uploaded successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Views pour Album
class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.prefetch_related('photos').all()
    serializer_class = AlbumSerializer
    
    
class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.prefetch_related('photos').all()
    serializer_class = AlbumSerializer

# Views pour Photo
class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class AlbumPhotosListView(ListAPIView):
    """
    Vue pour lister toutes les photos d'un album spécifique.
    """
    serializer_class = PhotoSerializer

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Photo.objects.filter(album_id=album_id)