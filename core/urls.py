from django.urls import path
from django.contrib.auth import views as auth_vievs
from . import views

urlpatterns = [
    path('', views.home, name = 'core-home'),
    path('register_teacher/', views.reg_tech, name = 'core-reg-tech'),
    path('register_student/', views.reg_stu, name = 'core-reg-stu'),
    path('about/', views.about, name = 'core-about'),
    path('login/', auth_vievs.LoginView.as_view(template_name='core/login.html'), name = 'core-login'),
    path('logout/', auth_vievs.LogoutView.as_view(template_name='core/logout.html'), name = 'core-logout'),

]