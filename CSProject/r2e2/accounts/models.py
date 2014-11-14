from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	Org = 'O'
	Faculty = 'F'
	Guest = 'G'
	SysAd = 'SA'
	BldgAd = 'BA'
	Chair = 'DC'

	User_Type_Choices = (
		(Org, 'Organization'),
		(Faculty, 'Faculty'),
		(Guest, 'Guest'),
		(SysAd, 'System Admin'),
		(BldgAd, 'Building Admin'),
		(Chair, 'Dept Chair'),
	)
	
	userType = models.CharField(max_length=2, choices=User_Type_Choices, default=SysAd)
	priorityLevel = models.IntegerField(default=0)
	additionalProperties = models.TextField(max_length=20)

	def __unicode__(self):
		return self.user.username
