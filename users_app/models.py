from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher=models.BooleanField(default=False, blank=False, null=False)
    is_student=models.BooleanField(default=False, blank=False, null=False)
    is_admin=models.BooleanField(default=False, blank=False, null=False)





    def __str__(self):
        return f'{self.user.username} Profil '

# Create your models here.
# class Student(User):
#     student = models.OneToOneField(User, on_delete= models.CASCADE)
#     is_active = False
#
#
#
#
#
#     def __str__(self):
#         return f'{self.student.username} Profil ucznia'
#
# class Teacher(models.Model):
#     teacher = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.teacher.username} Profil nauczyciela'