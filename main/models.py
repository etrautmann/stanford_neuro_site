from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.firstname + " " + self.lastname

class Faculty(models.Model):
    fullname = models.CharField(max_length = 40)
    email = models.CharField(max_length = 30)
    title = models.CharField(max_length = 80)
    website = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.fullname
