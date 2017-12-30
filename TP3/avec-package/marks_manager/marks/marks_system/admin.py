from django.contrib import admin
from .models import *

# Register your models here.
admin.register(Course, Examination, Student, Mark)(admin.ModelAdmin)