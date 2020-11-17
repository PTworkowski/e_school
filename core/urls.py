from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name = 'core-home'),
    path('about/', views.about, name = 'core-about'),
    path('', include('student_app.urls')),

]