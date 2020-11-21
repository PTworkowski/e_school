from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Subjects


# Create your views here.

#
# def subject_list(request):
#     subs = Subjects.objects.all()
#     return render(request, 'administration_app/subjects_app.html', {'subjects': subs})






"""class subject_management(request):
    if i_am_admin(request):
        model = Subject
        return 
def administation_app(request):
    if i_am_admin(request):
        pass
class SubjectManagement(ListView):
        model = Subject
        template_name = '/administration_app/subjects_app.html'
        pass
    def get_queryset(self):
        pass"""