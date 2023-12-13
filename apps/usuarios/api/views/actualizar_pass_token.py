from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.usuarios.models import RecuperarContraseña
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from apps.usuarios.api.serializers.usuario_serializer import PasswordSerializer
from rest_framework.permissions import AllowAny

class ActualizarContraseñaViewSet(viewsets.ViewSet):
    serializer_class = PasswordSerializer
    permission_classes = [AllowAny]


    def update(self, request, token):
        recuperar_contraseña = get_object_or_404(RecuperarContraseña, token=token)

        if recuperar_contraseña.expiracion < timezone.now():
            return Response({'message': 'El token ha caducado.'}, status=status.HTTP_400_BAD_REQUEST)

        if recuperar_contraseña.utilizado:
            return Response({'message': 'El token ya ha sido utilizado.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['password']

            user = recuperar_contraseña.usuario
            user.password = make_password(new_password)
            user.save()

            recuperar_contraseña.utilizado = True
            recuperar_contraseña.save()

            return Response({'message': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
