from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView
from library_app.models import Files
from .forms import UploadFile, UploadMultiFile
import os

# Create your views here.
@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            file_ob = form.save(commit=False)
            file_ob.owner = request.user
            if file_ob.title is None:
                file_path = str(file_ob.file.path).split('\\')
                file_ob.title = file_path[-1]
            file_ob.save()
            messages.success(request, f'Dodano plik')
            return redirect('library-upload')
    else:
        form = UploadFile()
    context = {
        'form': form,
    }
    return render(request, 'library_app/upload_form.html', context)

@login_required
def multi_upload(request):
    if request.method == 'POST':
        form = UploadMultiFile(request.POST, request.FILES)
        files= request.FILES.getlist('file')
        file_form_temp = form.save(commit=False)
        subject = file_form_temp.subject
        title = file_form_temp.title
        if form.is_valid():
            for f in files:
                file_ob = Files(file=f, subject=subject, title=title)
                file_ob.owner = request.user
                if file_ob.title is None:
                    file_path = str(file_ob.file.path).split('\\')
                    file_ob.title = file_path[-1]
                file_ob.save()
            messages.success(request, f'Dodano pliki')
            return redirect('library-upload')

    else:
        form = UploadMultiFile()
    context = {
        'form': form,
    }
    return render(request, 'library_app/upload_form.html', context)