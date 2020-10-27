from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'core-home'),
    path('register_teacher', views.reg_tech, name = 'core-reg-tech'),
    path('register_student', views.reg_stu, name = 'core-reg-stu'),
    path('about', views.about, name = 'core-about'),

]