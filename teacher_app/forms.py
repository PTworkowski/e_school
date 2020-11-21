from django import forms
from administration_app.models import Course


# class UploadMaterialsForm(forms.Form):
#     Tytuł = forms.CharField(max_length=50)
#     file = forms.FileField(label="Wybierz plik do dodania")

class SendLinkForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["zoom_link", "subject"]