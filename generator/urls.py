from django.contrib import admin
from django.urls import path,include
from generator import views


urlpatterns = [
    path('',views.home,name="home"),
    path('generated_password',views.password,name="password"),
    path('about_us',views.about,name="about"),

]