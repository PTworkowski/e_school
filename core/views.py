from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeacherRegisterForm, StudentRegisterForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def login(request):
    return render(request, 'core/login.html')

def reg_tech(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('core-home')
    else:
        form = TeacherRegisterForm
    return render(request, 'core/registration_teacher.html', {'form': form})

def reg_stu(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('core-home')
    else:
        form = StudentRegisterForm
    return render(request, 'core/registration_student.html', {'form': form})