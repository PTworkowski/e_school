from django.urls import path
from django.contrib.auth import views as auth_vievs
from . import views

urlpatterns = [
    path('',auth_vievs.LoginView.as_view(template_name= 'teacher_app/dashboard.html'), name = 'teacher-dashboard'),
    path('send_link/', views.send_link, name = 'send-link'),
    # path('materials_management', views.materials_management, name ='materials-management'),
    path('upload/', views.MeterialsManagementView.as_view(template_name= 'teacher_app/file_upload.html'), name='materials_upload'),
    ]