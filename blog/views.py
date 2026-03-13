from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignupForm


# Post List View
def post_list(request):
   posts = Post.objects.filter(status='published')
   return render(request, 'blog/post_list.html', {'posts': posts})


# Post Detail View
def post_detail(request, slug):
   post = get_object_or_404(Post, slug=slug, status='published')
   return render(request, 'blog/post_detail.html', {'post': post})


# Post Create View
@login_required
def post_create(request):
   if request.method == 'POST':

      form = PostForm(request.POST)

      if form.is_valid():

         post = form.save(commit=False)
         post.author = request.user
         post.save()
         form.save_m2m()
         return redirect('post_list')
   else:
      form = PostForm()

   return render(request, 'blog/post_form.html', {'form': form})


# Post Update View
@login_required
def post_update(request, slug):

   post = get_object_or_404(Post, slug=slug)

   form = PostForm(request.POST or None, instance=post)

   if form.is_valid():

      form.save()

      return redirect('post_detail', slug=post.slug)

   return render(request, 'blog/post_form.html', {'form': form})



# Post Delete View
@login_required
def post_delete(request, slug):

   post = get_object_or_404(Post, slug=slug)

   if request.method == 'POST':

      post.delete()

      return redirect('post_list')

   return render(request, 'blog/post_confirm_delete.html', {'post': post})

   
# User Signup View
def signup_view(request):

   if request.method == 'POST':

      form = SignupForm(request.POST)

      if form.is_valid():

         user = form.save()
         login(request, user)
         return redirect('post_list')

   else:

      form = SignupForm()

   return render(request, 'registration/signup.html', {'form': form})














      

