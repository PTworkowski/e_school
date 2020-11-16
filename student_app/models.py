from django.db import models
from django.db.models import CharField, Model, ForeignKey, CASCADE, BooleanField

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=225)
    subject = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    zoom_link = models.CharField(max_length=225)
    level = models.CharField(max_length=225)
    teacher = models.ForeignKey(Users, on_delete = models.CASCADE)
    student = models.ForeignKey(Users, on_delete = models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Student_courses(models,Model):
    student = models.ForeignKey(Users, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    payment = models.BooleanField()

    def __str__(self):
        return self.course

class Zoom_link(models.Model):
    meeting_link = models.URLField(max_length=200)

    def __str__(self):
        return self.meeting_link

class Course_materials(models.Model):
    file = models.ForeignKey(Files,on_delete = models.CASCADE)

    def __str__(self):
        return self.file
