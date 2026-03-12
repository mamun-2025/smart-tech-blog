from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify 


# Category models here
class Category(models.Model):
   name = models.CharField(max_length=100, unique=True) 
   slug = models.SlugField(max_length=120, unique=True, blank=True)

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name) 
      super().save(*args, **kwargs) 
   
   def __str__(self):
      return self.name 
   

# Tag models here 
class Tag(models.Model):
   name = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=120, unique=True, blank=True) 

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name) 
      super().save(*args, **kwargs)

   def __str__(self):
      return self.name 
   

# Post models here 
class Post(models.Model):
   STATUS_CHOICES = (
      ('draft', 'Draft'),
      ('published', 'Published')
   )

   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=220, unique=True, blank=True)
   content = models.TextField() 
   author =models.ForeignKey(User, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
   tags = models.ManyToManyField(Tag, blank=True)
   status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   published_at = models.DateTimeField(null=True, blank=True)

   class Meta: 
      ordering = ['-created_at']

   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      super().save(*args, **kwargs)

   def __str__(self):
      return self.title 
   

# Comment models here 
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commnets') 
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   active = models.BooleanField(default=True)

   def __str__(self):
      return f"Comment by {self.author.username} on {self.post.title}"
   

# Like/Reaction models here
class Like(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      unique_together = ('post', 'author')

   def __str__(self):
      return f"{self.author.username} likes {self.post.title}"