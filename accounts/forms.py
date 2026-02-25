
from django import forms 
from django.contrib.auth.models import User 
from .models import Profile

class UserUpdateForm(forms.ModelForm):
   email = forms.EmailField()
   fields =['username', 'email']

   class Meta:
      model = User
      fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = ['bio', 'profile_pic', 'website_url']

   
