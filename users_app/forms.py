from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users_app.models import MyUser, Adres

class CustomUserRegisterForm(UserCreationForm):


    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserAdresUpdateForm(forms.ModelForm):

    class Meta:
        model=Adres
        fields=['adres', 'city', 'zip_code']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email']