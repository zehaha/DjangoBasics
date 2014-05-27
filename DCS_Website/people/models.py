from django.db import models

class Faculty(models.Model):
    """Model for faculty"""
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='faculty_photos/')
    position = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    consultation = models.CharField(max_length=200, blank=True, null=True)
    research = models.CharField(max_length=225, blank=True, null=True)
    def __str__(self):
        return ("%s, %s %s"%(self.last_name,self.first_name,self.middle_name))

class Student(models.Model):
    """Model for students"""
    org_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='org_logos/')
    def __str__(self):
        return self.org_name
		
class Staff(models.Model):
    """Model for staff"""
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    def __str__(self):
        return ("%s, %s %s"%(self.last_name,self.first_name,self.middle_name))
