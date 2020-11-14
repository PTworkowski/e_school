from django import forms

class UploadMaterialsForm(forms.Form):
    Tytuł = forms.CharField(max_length=50)
    file = forms.FileField(label="Wybierz plik do dodania")