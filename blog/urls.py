
from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView, LogoutView 


urlpatterns = [
   
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/update/', views.post_update, name='post_update'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),

    path('signup/', views.signup_view, name='signup'),

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='post_list'), name='logout'),
    
]
