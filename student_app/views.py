from django.shortcuts import render, get_object_or_404
from administration_app.models import Course, GroupMaterials
from django.views.generic import ListView, DetailView
from django.conf import settings
from users_app.models import MyUser


# Create your views here.

class UserCourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'student_app/students_groups.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'student_app/course_detail.html'