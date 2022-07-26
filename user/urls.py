from django.urls import path
from .views import UserRegistration
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
   path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),  
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'), 

]