from django.urls import path
from library_app import views

urlpatterns = [
    path("upload/", views.multi_upload, name="library-upload"),
]
