from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.usuarios.api.serializers.usuario_serializer import (
    CustomTokenObtainPairSerializer, CustomUsuarioSerializer, CustomSerializerLogout)
from rest_framework_simplejwt.tokens import RefreshToken
from apps.usuarios.models import Usuario



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUsuarioSerializer(user)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh-token' : login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectas'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    serializer_class = CustomSerializerLogout

    def post(self, request, *args, **kwargs):
        user = Usuario.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesion cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario'}, status=status.HTTP_400_BAD_REQUEST)
