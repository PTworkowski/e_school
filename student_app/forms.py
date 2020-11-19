from django.forms import CharField,File
from django import forms

class View_link(forms.Form):
    id = forms.CharField(label="Materiały", max_length=100)

    class Meta:
        model = Files
        fields = ["title", "file", "subject"]