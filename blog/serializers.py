
from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
   author = serializers.StringRelatedField(read_only=True)
   likes_count = serializers.SerializerMethodField()

   class Meta:
      model = Post 
      fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'comments', 'tags', 'status', 'created_at', 'updated_at', 'published_at', 'likes_count']

   def get_likes_count(self, obj):
      return obj.likes.count() 
   

class CommentSerializer(serializers.ModelSerializer):
   author = serializers.StringRelatedField(read_only=True) 

   class Meta:
      model = Comment 
      fields = ['id' , 'post', 'author', 'content', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
   author = serializers.StringRelatedField(read_only=True)

   class Meta:
      model = Like 
      fields = ['id', 'post', 'author', 'created_at']