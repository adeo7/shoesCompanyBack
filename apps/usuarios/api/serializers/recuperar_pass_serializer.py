from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone

class RecuperarPassSerializer(serializers.Serializer):
    email = serializers.EmailField()

class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.is_active}"

password_reset_token_generator = CustomPasswordResetTokenGenerator()

def generate_reset_token(user):
    timestamp = int(timezone.now().timestamp())
    return password_reset_token_generator.make_token(user, timestamp)
