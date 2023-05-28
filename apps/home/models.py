# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30,null=False)
    password=models.CharField(max_length=150,null=False)
    create_date=models.DateTimeField(auto_now_add=True,null=True)
    state=models.BooleanField()

class Student(models.Model):
    name=models.CharField(max_length=150,null=False)
    lastname=models.CharField(max_length=180,null=False)
    bio=models.TextField()

class Mentor(models.Model):
    name=models.CharField(max_length=150,null=False)
    lastname=models.CharField(max_length=150,null=False)
    bio=models.TextField()
    state=models.BooleanField()

class Session(models.Model):
    mentor=models.ForeignKey(Mentor, on_delete=models.CASCADE)
    students= models.ManyToManyField(Student)


    

