from django.db import models
from users_app.models import MyUser
from library_app.models import Files
from core.models import Subjects
from django.conf import settings


# Create your models here.


class Schedule(models.Model):
    class DaysOfWeek(models.TextChoices):
        poniedzialek = 'Poniedziałek'
        wtorek = 'Wtorek'
        sroda = 'Środa'
        czwartek = 'Czwartek'
        piatek = 'Piątek'
        sobota = 'Sobota'
        niedziela = 'Niedziela'

    day = models.CharField(max_length=12, choices=DaysOfWeek.choices)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.day} {self.time}'


class Course(models.Model):
    name = models.CharField(max_length=225)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    zoom_link = models.URLField(max_length=255, default="", null=True, blank=True)
    level = models.CharField(max_length=225)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, default=None, null=True,
                                blank=True,
                                related_name='teacher')
    student = models.ManyToManyField(MyUser, through='StudentCourses',
                                     blank=True)
    schedule = models.ManyToManyField(Schedule, related_name='schedule', blank=True)

    def __str__(self):
        return self.name


class StudentCourses(models.Model):
    person = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.person} {self.course}'


class GroupMaterials(models.Model):
    id_files = models.ForeignKey(Files, related_name='files', on_delete=models.PROTECT)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)
