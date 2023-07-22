from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Profile
        fields = ['email', 'password', 'name', 'surname', 'city', 'image']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        profile = Profile.objects.create(
            user=user,
            name=validated_data['name'],
            surname=validated_data['surname'],
            city=validated_data['city'],
            image=validated_data['image']
        )
        return profile        