from django.db import models
from people.models import Faculty

# Create your models here.

class Lab(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	abbr = models.CharField(max_length=200)
	head = models.CharField(max_length=200)
	email = models.EmailField(max_length=200,blank=True, null=True)
	telephone =  models.CharField(max_length=200,blank=True, null=True)
	website = models.URLField(max_length=200, blank=True, null=True)
	logo = models.ImageField(upload_to='research_logos/',null=True,blank=True)
	def __str__(self):
		return self.name
		
class Field(models.Model):
	lab_name = models.ForeignKey(Lab)
	field_name = models.CharField(max_length=200)
	def __str__(self):
		return self.field_name

class Adviser(models.Model):
	lab_name = models.ForeignKey(Lab)
	adviser_name = models.ForeignKey(Faculty)
	def __str__(self):
		return str(self.adviser_name)
