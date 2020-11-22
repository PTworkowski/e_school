from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from django.views.generic import ListView

from administration_app.models import Course
from e_school.decorators import teacher_required
from teacher_app.forms import SendLinkForm


def teach_dash(request):
    return render(request, "teacher_app/dashboard.html")


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


class TeacherCourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'teacher_app/teacher_courses.html'
