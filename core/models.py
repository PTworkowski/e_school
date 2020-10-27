from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.student.username} Profil ucznia'

class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher.username} Profil nauczyciela'