from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_dash, name="admin-dashboard"),
    path("courses/", views.UserCourseListView.as_view(), name="admin-courses"),
    path("courses/<int:pk>", views.CourseDetailView.as_view(), name="admin-courses-detail"),

]
