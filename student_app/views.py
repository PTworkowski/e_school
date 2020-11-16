from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from users_app import views



def index(request):
    return HttpResponse("Zalogowałeś się poprawnie na swój profil")

def get_link(request):
    return render(request, 'teacher_app/send_link.html')
