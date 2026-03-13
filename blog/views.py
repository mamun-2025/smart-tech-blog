from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like
from .forms import PostForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignupForm, CommentForm


# Post List View
def post_list(request):
   posts = Post.objects.filter(status='published')
   return render(request, 'blog/post_list.html', {'posts': posts})


# Post Detail View
def post_detail(request, slug):
   post = get_object_or_404(Post, slug=slug, status='published')
   form = CommentForm()
   comments = post.comments.all()
   context = {
      'post': post,
      'comments': comments,
      'form': form,
   }
   return render(request, 'blog/post_detail.html', context)


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


# User Comment View
@login_required
def add_comment(request, slug):
   post = get_object_or_404(Post, slug=slug)

   if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.author = request.user 
         comment.post = post 
         comment.save()
         return redirect('post_detail', slug=post.slug)
   
   return redirect('post_detail', slug=post.slug)


# User Comment Delete View
@login_required
def delete_comment(request, comment_id):
   comment = get_object_or_404(Comment, id=comment_id)

   if request.user == comment.author:
      post_slug = comment.post.slug 
      comment.delete()
      return redirect('post_detail', slug=post_slug)

   return redirect('post_detail')


# User Likes View
@login_required
def toggle_like(request, slug):
   post = get_object_or_404(Post, slug=slug) 
   like, created = Like.objects.get_or_create(post=post, author=request.user)

   if not created:
      like.delete()

   return redirect('post_detail', slug=slug) 


















      

