

from django import forms 
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User PostForm
class PostForm(forms.ModelForm):
   class Meta:
      model = Post 
      fields = ['title', 'content', 'category', 'tags', 'status']
   

# User Registration Form
class SignupForm(UserCreationForm):

   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']
      

# User Comment Form
class CommentForm(forms.ModelForm):

   class Meta:
      model =Comment 
      fields = ['content']
      widgets = {
         'content': forms.Textarea(attrs={
            'rows': 3,
            'class': 'w-full border rounded p-2',
            'placeholder': 'Write your comment here...'
         }),
      }
