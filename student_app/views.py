from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from datetime import date

# Create your views here.
def get_link(request):
    return render(request, 'teacher_app/get_link.html')
