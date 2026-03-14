
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer 
from rest_framework import viewsets, permissions, filters 
from rest_framework.decorators import action 
from rest_framework.response import Response 

# Post ViewSet 
class PostViewSet(viewsets.ModelViewSet):
   queryset = Post.objects.filter(status='published')
   serializer_class = PostSerializer 
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   filter_backends = [filters.SearchFilter] 
   search_fields = ['title', 'content', 'author__username', 'category__name']

   def perform_create(self, serializer):
      serializer.save(author=self.request.user)

# Comment ViewSet 
class CommentViewSet(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer 
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def perform_create(self, serializer):
      serializer.save(author=self.request.user)

# Like ViewSet 
class LikeViewSet(viewsets.ModelViewSet):
   queryset = Like.objects.all()
   serializer_class = LikeSerializer 
   permission_classes = [permissions.IsAuthenticated] 

   @action(detail=False, methods=['post']) 
   def toggle_like(self, request):
      post_id = request.data.get('post')
      if not post_id:
         return Response({'error': 'Post ID is required'}, status=400)
      try: 
         post = Post.objects.get(id=post_id) 
         like, created = Like.objects.get_or_create(post=post, author=request.user)
         if not created:
            like.delete()
            return Response({'status': 'unliked', 'likes_count': post.likes.count()})
         return Response({'status': 'liked', 'likes_count': post.likes.count()})
      except Post.DoesNotExist:
         return Response({'error': 'Post not found'}, status=404)
   
