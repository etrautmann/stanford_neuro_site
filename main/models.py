from django.db import models
import datetime

class Student(models.Model):
		sunetid = models.CharField(max_length = 255,primary_key=True)
		Name = models.CharField(max_length = 255)
		NAME_FIRST = models.CharField(max_length = 255)
		NAME_LAST = models.CharField(max_length = 255)
		Email = models.CharField(max_length = 255)
		PI = models.CharField(max_length = 255)
		Department = models.CharField(max_length = 255)
		#firstname = models.CharField(max_length = 20)
		#lastname = models.CharField(max_length = 20)
		#email = models.CharField(max_length = 30)
		#image = models.CharField(max_length = 30)
		#lab = models.CharField(max_length = 50)
		#labwebsite = models.CharField(max_length = 100)

		def __unicode__(self):
			return self.Name
				#return self.firstname + " " + self.lastname
 		class Meta:
			db_table = 'students'
			managed = False

class Theme(models.Model):
		theme = models.CharField(max_length = 3)
		fulltheme = models.CharField(max_length = 30)

		def __unicode__(self):
				return self.fulltheme

class Faculty(models.Model):
		sunetid = models.CharField(max_length = 255,primary_key=True)
		firstname = models.CharField(max_length = 20)
		lastname = models.CharField(max_length = 255)
		email = models.CharField(max_length = 255)
		location = models.CharField(max_length = 60)
		Interests = models.CharField(max_length = 70)
		Summary = models.TextField()
		Disease = models.IntegerField()
		Systems = models.IntegerField()
		Cellular = models.IntegerField()
		Molecular = models.IntegerField()
		Developmental = models.IntegerField()
		Excitability = models.IntegerField()
		Computational = models.IntegerField()
		website = models.CharField(max_length = 255)
		mentor = models.IntegerField()

		def __unicode__(self):
				return self.firstname + " " + self.lastname
 		class Meta:
			db_table = 'faculty'
			managed = False

class Alumnus(models.Model):
		id = models.IntegerField(primary_key=True)
		LastName = models.CharField(max_length = 255)
		FirstName = models.CharField(max_length = 255)
		NickName = models.CharField(max_length = 255)
		YearGraduated = models.IntegerField()
		CurrentPosition = models.CharField(max_length = 255)
		Website = models.CharField(max_length = 255)
		Advisor = models.CharField(max_length = 255)
		email = models.CharField(max_length = 255)

		def __unicode__(self):
				return self.FirstName + " " + self.LastName

		class Meta:
			db_table = 'alumni'
			managed = False

class Course(models.Model):
		#QUARTER_CHOICES = (
						#(1,'Autumn'),
						#(2,'Winter'),
						#(3,'Spring'),
						#)
		#CONCENTRATION_CHOICES = (
		#				(1,'Cellular/Molecular/Developmental'),
		#				(2,'Translational'),
		#				(3,'Systems/Behavioral/Computational'),
		#				)
		#YEAR_CHOICES = (
		#				(0,'This Year'),
		#				(1,'Both this and next year'),
		#				(2,'Next Year')
		#				)
		#department = models.CharField(max_length=10)
		#number = models.CharField(max_length=4)
		#title = models.CharField(max_length=80)
		#concentration = models.IntegerField(choices = CONCENTRATION_CHOICES)
		#quarter = models.IntegerField(choices = QUARTER_CHOICES)
		#schoolyear = models.IntegerField(choices = YEAR_CHOICES)
		#professors = models.CharField(max_length=50)
		#description = models.CharField(max_length=2000)
		id = models.IntegerField(primary_key=True)
		Title = models.CharField(max_length = 255)
		Faculty1 = models.CharField(max_length = 255)
		Faculty2 = models.CharField(max_length = 255)
		Faculty3 = models.CharField(max_length = 255)
		Dept = models.CharField(max_length = 255)
		Course_Number = models.CharField(max_length = 255)
		Credits = models.IntegerField()
		Quarter_Offered = models.CharField(max_length = 255)
		Next_Offered = models.CharField(max_length = 255)
		Course_Description = models.TextField()
		notes = models.CharField(max_length = 255)
		Area_Fulfill = models.CharField(max_length = 255)
		Frequency = models.CharField(max_length = 255)
		
		def __unicode__(self):
				return self.Dept + " " + self.Course_Number
		
		#def get_year(self):
				#year = datetime.datetime.now().year
				#month = datetime.datetime.now().month
				#if month < 9:
						#if self.schoolyear <= 1:
								#return str(year-1) + "-" + str(year)
						#else:
								#return str(year) + "-" + str(year+1)
				#else:
						#if schoolyear <= 1:
								#return str(year) + "-" + str(year+1)
						#else:
								#return str(year+1) + "-" + str(year+2)

		#def get_quarter(self):
				#if self.quarter == 1:
						#return "Autumn"
				#elif self.quarter == 2:
						#return "Winter"
				#elif self.quarter == 3:
						#return "Spring"
				#elif self.quarter == 4:
						#return "Summer"

		#def get_concentration(self):
				#if self.concentration == 1:
						#return "Cellular/Molecular/Developmental"
				#elif self.concentration == 2:
						#return "Translational"
				#elif self.concentration == 3:
						#return "Systems/Behavioral/Computational"
		class Meta:
			db_table = 'courses'
			managed = False


class FAQ(models.Model):
		question = models.TextField()
		answer = models.TextField()

		def __unicode__(self):
				return self.question
