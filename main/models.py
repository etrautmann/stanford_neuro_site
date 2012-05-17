from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)

class Faculty(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    position = models.CharField(max_length = 20)
