
from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag('blog/post/lastest_posts.html')
def show_latest_posts(count=5):
   lastest_posts = Post.objects.filter(status='Published').order_by('-publish')[:count]
   return {'lastest_posts': lastest_posts}


