from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    age=models.IntegerField()

from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','course','age']
admin.site.register(Student,StudentAdmin)
