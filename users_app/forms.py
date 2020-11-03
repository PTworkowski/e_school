from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users_app.models import MyUser

class StudentRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




class TeacherRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']