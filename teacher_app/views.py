from django.shortcuts import render, redirect,reverse
from django.views.generic import CreateView, FormView, UpdateView
# from .forms import UploadMaterialsForm
from .models import File
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from e_school.decorators import teacher_required
from django.shortcuts import render, get_object_or_404
from administration_app.models import Course, GroupMaterials
from django.views.generic import ListView, DetailView
from django.contrib import messages
from teacher_app.forms import SendLinkForm
from django.conf import settings
from users_app.models import MyUser


# def send_link(request):
#     return render(request,'teacher_app/send_link.html')

@login_required
@teacher_required
def send_link(request):
    if request.method == "POST":
        form = SendLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Wysłano link do grupy!")
            return reverse(redirect("teacher_app/dashboard.html"))
    else:
        form = SendLinkForm
    return render(request, "teacher_app/send_link.html", {'form': form})


# class SendLinkUpdateView(UpdateView):
#     model = Course
#     template_name = "teacher_app/teacher-dashboard.html"

# @login_required
# class TeacherCourseListView(ListView):
#     context_object_name = 'courses'
#     template_name = 'teacher_app/send_link.html'
#
#     def query_set(request):
# #         queryset = Course.objects.filter(teacher=MyUser)
#
#         return queryset
#
# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'student_app/course_detail.html'
#
class TeacherCourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'teacher_app/teacher_courses.html'