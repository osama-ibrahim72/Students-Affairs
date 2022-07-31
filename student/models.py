import email
from django.db import models

# Create your models here.

class Student(models.Model):
    lvls = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    ]
    depts = [
        ('AI','AI'),
        ('CS','CS'),
        ('IS','IS'),
        ('IT','IT'),
        ('DS','DS'),
    ]
    name = models.CharField(max_length=256)
    sid = models.IntegerField()
    dateOfBirth = models.DateField()
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    lvl = models.CharField(max_length=1,)
    Status = models.BooleanField(default=True)
    depart = models.CharField(max_length=10,)
    email = models.CharField(max_length=256)
    mobileNum = models.CharField(max_length=11)
    def __str__(self):
        return self.name

class Courses (models.Model):
    depts = [
        ('AI','AI'),
        ('CS','CS'),
        ('IS','IS'),
        ('IT','IT'),
        ('DS','DS'),
    ]
    name = models.CharField(max_length=256)
    cid = models.CharField(max_length=16)
    depart = models.CharField(max_length=2)
    students = models.ForeignKey(Student,on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    def __str__(self):
        return self.name


