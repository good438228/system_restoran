from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='global_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]