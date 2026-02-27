
from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'body', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'rows': 5}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

