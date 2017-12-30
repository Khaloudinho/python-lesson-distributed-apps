from django.db import models
from django.utils import timezone

import datetime
# Create your models here.
class Examination(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateTimeField('examination date')

    def __str__(self):
        return self.name

class Student(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date')

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' birthDate : ' + str(self.birth_date)

class Course(models.Model):
    code = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    students = models.ManyToManyField(Student)
    # students = models.ManyToManyField(Student, on_delete=models.CASCADE)
    examination = models.OneToOneField(
        Examination,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.code

class Mark(models.Model):
    mark = models.DecimalField(decimal_places=2, max_digits=4)

    students = models.ManyToManyField(Student)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.mark)