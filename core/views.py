from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.forms import TeacherRegisterForm, StudentRegisterForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

