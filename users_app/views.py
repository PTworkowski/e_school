from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.forms import StudentRegisterForm, TeacherRegisterForm

# Create your views here.
def login(request):
    return render(request, 'users_app/login.html')

def reg_tech(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.is_teacher = True
            tech.is_active = False
            tech.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('users-login')
    else:
        form = TeacherRegisterForm
    return render(request, 'users_app/registration_teacher.html', {'form': form})

def reg_stu(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            stud.is_student = True
            stud.is_active = False
            stud.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('users-login')
    else:
        form =StudentRegisterForm
    return render(request, 'users_app/registration_student.html', {'form': form})