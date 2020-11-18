from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='administration_app/administration_profil.html'), name='administration-profil'),
    path('subjects/', views.subject_list, name='subjects-profile'),
]