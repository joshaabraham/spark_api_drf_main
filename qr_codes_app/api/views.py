import qrcode
from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from rest_framework import generics
from qr_codes_app.models import QRCode
from .serializers import QRCodeSerializer

class QRCodeListCreateView(generics.ListCreateAPIView):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

class QRCodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

class QRCodeImageView(generics.RetrieveAPIView):
    queryset = QRCode.objects.all()

    def get(self, request, *args, **kwargs):
        qr_code = self.get_object()
        img = qrcode.make(qr_code.content)
        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)
        image_data = img_io.getvalue()

        return JsonResponse({"image": image_data.hex()})