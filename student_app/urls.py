from django.urls import path
from django.contrib.auth import views as auth_vievs
from. import views

urlpatterns = [
    path('',auth_vievs.LoginView.as_view(template_name= 'student_app/dashboard.html'), name= 'student-dashboard'),
    path('get_link/', views.get_link, name = 'get-link'),
    path('',v

]