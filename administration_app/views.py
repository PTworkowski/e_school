from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Subjects


# Create your views here.


def subject_list(request):
    subs = Subjects.objects.all()
    return render(request, 'administration_app/subjects_app.html', {'subjects': subs})



