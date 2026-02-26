from django.db import models 
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   bio = models.TextField(blank=True)
   profile_pic = CloudinaryField('image', folder='profile_pics')
   website_url = models.URLField(max_length=200, blank=True)

   def __str__(self):
      return f'{self.user.username} Profile'
   
   
