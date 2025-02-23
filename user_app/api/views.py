
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

import jwt, datetime
from profile_app.models import ProfileUser
from comportement_app.models import UserComportement
from user_config.models import UserConfiguration
from user_app.api.serializers import ComportementSerializer, ConfigurationSerializer, ProfileSerializer, UserSerializer
from user_app.models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        # Generate tokens using SimpleJWT
        refresh = RefreshToken.for_user(user)
        
         # Get user profile and configuration
        profile = ProfileUser.objects.get(user=user)
        # configuration = UserConfiguration.objects.get(user=user)
        # comportement = UserComportement.objects.get(user=user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data,
            'profile': ProfileSerializer(profile).data,
            # 'configuration': ConfigurationSerializer(configuration).data,
            # 'comportement': ComportementSerializer(comportement).data,
        })


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response