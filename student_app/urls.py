from django.urls import path
from student_app import views

urlpatterns = [
    path("", views.stud_dash, name="student-dashboard"),
    path("courses/", views.UserCourseListView.as_view(), name="student-courses"),
    path(
        "courses/<int:pk>",
        views.CourseDetailView.as_view(),
        name="student-courses-detail",
    ),
]
