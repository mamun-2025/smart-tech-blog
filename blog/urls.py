
from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    # ক্যাটাগরি ফিল্টারের জন্য এই পাথটি যোগ করুন
    path('category/<slug:category_slug>/', views.PostListView.as_view(), name='post_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]




