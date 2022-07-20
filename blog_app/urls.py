from  django.urls import path 
from .views import index,blogs,add_post, update_post ,delete_post

urlpatterns = [
    path('index/',index.as_view(),name='index'),
    path('blogs/<int:pk>',blogs.as_view(),name="blogs"),
    path('add_post',add_post.as_view(),name='add_post'),
    path('blogs/edit/<int:pk>',update_post.as_view(),name='update_post'),
    path('blogs/<int:pk>/delete',delete_post.as_view(),name='delete_post'),
   
    
]