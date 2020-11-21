from django.contrib import admin
from .models import Course, Schedule, GroupMaterials, StudentCourses


admin.site.register(Schedule)
admin.site.register(Course)
admin.site.register(GroupMaterials)
admin.site.register(StudentCourses)
