from django.urls import path
from django.contrib.auth import views as auth_vievs
from . import views

urlpatterns = [
    path('login/', auth_vievs.LoginView.as_view(template_name= 'users_app/login.html'), name = 'users-login'),
    path('logout/', auth_vievs.LogoutView.as_view(template_name= 'users_app/logout.html'), name = 'users-logout'),
    path('reg_stu/', views.reg_stu, name = 'users-reg-stu'),
    path('reg_tech/', views.reg_tech, name = 'users-reg-tech'),


]