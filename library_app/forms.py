from .models import Files
from django.forms import ClearableFileInput
from django import forms


class UploadFile(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Files
        fields = ["title", "file", "subject"]


class UploadMultiFile(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Files
        fields = ["title", "file", "subject"]
