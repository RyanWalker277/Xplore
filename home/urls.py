from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index , name ="home"),
    path("login", views.login , name ="login"),
    path("purchase", views.purchase , name ="purchase"),
    path("register", views.register , name ="register"),
    path("dashboard", views.dashboard , name ="dashboard"),
    path("search/", views.search_result , name ="search"),
    path("KIET", views.kiet_page , name ="kiet_page"),
    path("done", views.done , name ="done"),
    path("profile_settings", views.profile_settings , name ="profile_settings"),
    path("save", views.save , name ="save"),
    path("JSS",views.jss_page,name="jss_page"),
    path("AKGEC",views.akgec,name="akgec_page"),
    
]
