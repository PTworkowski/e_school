
from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.forms import UserUpdateForm, UserAdresUpdateForm, CustomUserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'users_app/login.html')

def reg_tech(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.is_teacher = True
            tech.is_active = True
            tech.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('users-login')
    else:
        form = CustomUserRegisterForm
    return render(request, 'users_app/registration_teacher.html', {'form': form})

def reg_stu(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            stud = form.save(commit=False)
            stud.is_student = True
            stud.is_active = True
            stud.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stworzono konto dla {username}! Poczekaj na aktywację przez administrację')
            return redirect('users-login')
    else:
        form =CustomUserRegisterForm
    return render(request, 'users_app/registration_student.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserAdresUpdateForm(request.POST, instance=request.user.adres)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has bean updated')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserAdresUpdateForm(instance=request.user.adres)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users_app/profile.html', context)