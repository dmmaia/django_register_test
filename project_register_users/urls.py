from django.contrib import admin
from django.urls import path
from app__register_users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.users, name='users_list')
]
