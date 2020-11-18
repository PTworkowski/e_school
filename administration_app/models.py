from django.db import models
from users_app.models import MyUser



# Create your models here.


class Subjects(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.day} {self.time}'


class Course(models.Model):
    name = models.CharField(max_length=225)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    zoom_link = models.URLField(max_length=255)
    level = models.CharField(max_length=225)
    teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    student = models.ManyToManyField('users_app.models.MyUser') #Tutaj sie coś nie zgadza
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#Nie wiem czy to jest poprawne, myśle że to jest niepotrzebne????
class GroupMaterials(models.Model):
    id_filles = models.ManyToManyField('library_app.models.Files')
    id_course = models.ManyToManyField('library_app.models.Files')