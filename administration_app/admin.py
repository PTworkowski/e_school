from django.contrib import admin
from .models import Course, Schedule, GroupMaterials

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'zoom_link','level','teacher')


admin.site.register(Schedule)
admin.site.register(GroupMaterials)
