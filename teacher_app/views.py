from django.shortcuts import render
from django.views.generic import CreateView, FormView
from .forms import UploadMaterialsForm
from .models import File
from django.http import HttpResponseRedirect

def send_link(request):

    return render(request,'teacher_app/send_link.html')

class MeterialsManagementView(FormView):
    template_name = "teacher_app/file_upload.html"
    form_class = UploadMaterialsForm

    def upload_materials(self, form):
        uploaded_file = File(
            file=self.get_form_kwargs().get('materials')['file'])
        uploaded_file.save()
        self.id = uploaded_file.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(request):
        return render(request,'teacher_app/materials_management')
