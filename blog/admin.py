from django.contrib import admin
from .models import Category, Tag, Post, Comment, Like


class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'content', 'author', 'category', 'status', 'created_at')
   list_filter = ('status', 'author', 'category')
   search_fields = ('title', 'content')
   prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment) 
admin.site.register(Like)

