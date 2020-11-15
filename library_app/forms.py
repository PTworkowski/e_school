from .models import Files
from django import forms

class UploadFile(forms.ModelForm):
    file= forms.FileField()

    class Meta:
        model= Files
        fields= ['title', 'file', 'subject']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)