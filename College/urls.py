from turtle import home
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('login',include('home.urls')),
    path('purchase',include('home.urls')),
    path('register',include('home.urls')), 
    path('dashboard',include('home.urls')),
    path('search_result',include('home.urls')),
    path('kiet_page',include('home.urls')),
    path('done',include('home.urls')),
    path('profile_settings',include('home.urls')),
    path('save',include('home.urls')),
]
