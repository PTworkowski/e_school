from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return HttpResponse("Zalogowałeś się poprawnie na swój profil")


