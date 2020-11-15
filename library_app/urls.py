from django.urls import path
from library_app import views

urlpatterns = [
    path('upload/', views.upload, name = 'library-upload'),

]