from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'slug')
   prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug', 'author', 'publish', 'status')
   list_filter = ('status', 'created', 'publish', 'author')
   search_fields = ('title', 'body')
   prepopulated_fields = {'slug': ('title',)}
   raw_id_fields = ('author',)
   date_hierarchy = 'publish'
   ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   list_display = ('post', 'name', 'email', 'created', 'active')
   list_filter = ('active', 'created', 'updated')
   search_fields = ('name', 'email', 'body')
   actions = ['approve_comments']

   def approve_comments(self, request, queryset):
      queryset.update(active=True)






































