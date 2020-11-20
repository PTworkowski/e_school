from django.db import models
from users_app.models import MyUser
#from library_app.models import Files



# Create your models here.

class Subjects(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


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
    zoom_link = models.URLField(max_length=255, blank=True)
    level = models.CharField(max_length=225)
    teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='teacher')
    student = models.ManyToManyField(MyUser, related_name='students')
    schedule = models.ManyToManyField(Schedule, related_name='schedule')
    materials = models.ManyToManyField

    def __str__(self):
        return self.name



"""#Nie wiem czy to jest poprawne, myśle że to jest niepotrzebne????
class GroupMaterials(models.Model):
    id_files = models.ManyToManyField(Files related_name='files')
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)
"""