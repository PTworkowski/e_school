from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, DetailView

from administration_app.models import Course, StudentCourses


def admin_dash(request):
    return render(request, "administration_app/dashboard.html")

class UserCourseListView(ListView):
    model = Course
    context_object_name = 'student_courses'
    template_name = 'administration_app/admin_groups.html'



class CourseDetailView(DetailView):
    model = StudentCourses
    template_name = 'administration_app/course_detail.html'
