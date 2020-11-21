from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_teacher = models.BooleanField(default=False, blank=False, null=False)
    is_student = models.BooleanField(default=False, blank=False, null=False)
    is_admin = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=120, default="", null=True, blank=True)
    building = models.CharField(max_length=20, default="", null=True, blank=True)
    apartment = models.CharField(max_length=20, default="", null=True, blank=True)
    city = models.CharField(max_length=20, default="", null=True, blank=True)
    zip_code = models.CharField(max_length=6, default="", null=True, blank=True)