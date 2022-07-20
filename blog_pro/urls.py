from django.contrib import admin
from django.urls import path , include
from blog_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_app.urls')),
    path('',index.as_view(),name='index'),
    path('accounts/',include('user.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    

]
