

from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Category, Comment
from django.db.models import Q
from .forms import CommentForm, PostForm
from django.views.generic.edit import CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin



class PostListView(ListView):
   model = Post
   template_name = 'blog/post/list.html'
   context_object_name = 'posts'
   paginate_by = 5

   def get_queryset(self):
      queryset = Post.objects.filter(status='published')

      # সার্চ লজিক যোগ করা
      search_query = self.request.GET.get('q') 
      if search_query:
         queryset = queryset.filter(
             Q(title__icontains=search_query) | Q(body__icontains=search_query)
             )
         
  # ইউআরএল থেকে ক্যাটাগরি স্ল্যাগ চেক করা (ফিল্টারিং লজিক)
      category_slug = self.kwargs.get('category_slug')
      if category_slug:
         queryset = queryset.filter(category__slug=category_slug)

      return queryset 
   
   
   def get_context_data(self, **kwargs):
      # সাইডবারে সব ক্যাটাগরি দেখানোর জন্য অতিরিক্ত ডেটা পাঠানো
      context = super().get_context_data(**kwargs) 
      context['categories'] = Category.objects.all() 

      # সার্চ করা শব্দটা টেমপ্লেটে ধরে রাখার জন্য
      context['search_query'] = self.request.GET.get('q')
      
      # বর্তমানে কোন ক্যাটাগরি সিলেক্ট করা আছে সেটা জানানো
      if self.kwargs.get('category_slug'):
         context['current_category'] = Category.objects.get(slug=self.kwargs['category_slug'])
      return context




class PostDetailView(DetailView, FormMixin): # FormMixin যোগ করা হয়েছে
   model = Post
   template_name = 'blog/post/detail.html'
   context_object_name = 'post'
   slug_url_kwarg = 'slug' 
   query_pk_and_slug = False # আমরা শুধু স্ল্যাগ দিয়ে খুঁজব
   form_class = CommentForm # কোন ফর্মটি ব্যবহার হবে তা বলে দেওয়া
 
   def get_success_url(self):
      # কমেন্ট সেভ হওয়ার পর আবার এই পেজেই ফিরে আসবে
      return self.get_object().get_absolute_url()
   
   
   def get_context_data(self, **kwargs):
      # ডিটেইল পেজেও সাইডবার থাকবে, তাই ক্যাটাগরি ডেটা এখানেও পাঠাতে হবে
      context = super().get_context_data(**kwargs) 
      context['categories'] = Category.objects.all()
      # বর্তমানে পোস্টের যে কমেন্টগুলো 'active' আছে সেগুলো পাঠানো
      context['comments'] = Comment.objects.filter(active=True) 
      # ফর্মটি কন্টেক্সটে পাঠানো (FormMixin এটি অটো করে, তবুও স্পষ্ট থাকল)
      context['comment_form'] = self.get_form()
      return context
   
   def post(self, request, *args, **kwargs):
      # ইউজার যখন ফর্ম সাবমিট করবে তখন এই মেথড কল হবে
      self.object = self.get_object()
      form = self.get_form()
      if form.is_valid():
         return self.form_valid(form)
      else:
         return self.form_invalid(form)
      
   def form_valid(self, form):
      # ফর্মটি ভ্যালিড হলে কমেন্ট সেভ করা হবে
      comment = form.save(commit=False)
      comment.post = self.object
      comment.save()
      return super().form_valid(form)
   

class AboutPageView(TemplateView):
   template_name = 'blog/post/about.html'

class ContactPageView(TemplateView):
   template_name = 'blog/post/contact.html'


class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   form_class = PostForm
   template_name = 'blog/post/post_form.html'

   def get_success_url(self):
      return '/'
   
   def form_valid(self, form):
      form.instance.author = self.request.user

      form.instance.status = 'published'
      return super().form_valid(form)
   

   