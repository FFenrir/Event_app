from rest_framework import serializers

from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)
    is_superuser = serializers.BooleanField(default=False)


    class Meta:
        model = User
        fields = ('id', 'email', 'password','is_staff', 'is_superuser', 'is_active',)