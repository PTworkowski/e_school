from django.contrib import admin
from .models import Subjects, Course, Schedule

# Register your models here.
admin.site.register(Subjects)
admin.site.register(Course)
admin.site.register(Schedule)
