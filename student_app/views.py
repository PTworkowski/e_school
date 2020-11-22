from django.shortcuts import render, get_object_or_404
from administration_app.models import Course, GroupMaterials, StudentCourses
from django.views.generic import ListView, DetailView
from django.conf import settings
from users_app.models import MyUser
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# Create your views here.


def stud_dash(request):
    return render(request, "student_app/dashboard.html")


class UserCourseListView(ListView):
    model = Course
    context_object_name = 'student_courses'
    template_name = 'student_app/students_groups.html'



class CourseDetailView(DetailView):
    model = StudentCourses
    template_name = 'student_app/course_detail.html'
