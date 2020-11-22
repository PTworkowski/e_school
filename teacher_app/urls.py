from django.urls import path
from . import views

urlpatterns = [
    path("", views.teach_dash, name="teacher-dashboard"),
    path("send_link/", views.send_link, name="send-link"),
    path("courses/", views.TeacherCourseListView.as_view(), name="teacher-course-list"),
]
