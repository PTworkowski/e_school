from django.contrib import admin
from .models import MyUser, Address

admin.site.register(MyUser)
admin.site.register(Address)