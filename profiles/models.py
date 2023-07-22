import os
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.dispatch import receiver



# Create your models here.
def get_profile_image_path(instance, filename):
    user_name = instance.name
    user_surname = instance.surname
    user_id = instance.id
    folder_name = f'{user_id}_{user_name}_{user_surname}'.replace(" ", "_")  # Replace spaces with underscores
    folder_path = os.path.join('media', 'profile_pictures', folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return os.path.join(folder_path, filename)

class Profile(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    image = models.ImageField(upload_to = get_profile_image_path,blank=False,max_length=100,default='default.jpg')
    city = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('profile_details', args=[str(self.id)])

    def __str__(self):
        return f"{self.name}, {self.city}"
    

