from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.firstname + " " + self.lastname

class Faculty(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    degree = models.CharField(max_length = 20)
    website = models.CharField(max_length = 100)
    title = models.CharField(max_length = 20)
    department = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30)
    blurb = models.CharField(max_length = 4000)

    def __unicode__(self):
        return self.firstname + " " + self.lastname
