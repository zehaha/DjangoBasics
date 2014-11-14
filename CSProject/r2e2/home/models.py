from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Rooms(models.Model):
	roomName = models.CharField(max_length=20)
	roomType = models.CharField(max_length=20)
	roomNumber = models.IntegerField()
	capacity = models.IntegerField()

	def __unicode__(self):
		return self.roomName

	class Meta:
		verbose_name_plural = 'Rooms'

class Events(models.Model):
	eventName = models.CharField(max_length=20)
	eventType = models.CharField(max_length=20)
	created_by = models.ForeignKey(UserProfile, related_name='events_created_by')
	approved_by = models.ForeignKey(UserProfile, related_name='events_approved_by')
	approvalStatus = models.CharField(max_length=30)

	def __unicode__(self):
		return self.eventName

	class Meta:
		verbose_name_plural = 'Events'

class Schedules(models.Model):
	startTime = models.TimeField()
	endTime = models.TimeField()
	date = models.DateField()
	event = models.ForeignKey(Events)

	class Meta:
		verbose_name_plural = 'Schedules'

class Requests(models.Model):
	event = models.ForeignKey(Events)
	schedule = models.ForeignKey(Schedules)
	room = models.ForeignKey(Rooms)
	requestedBy = models.ForeignKey(UserProfile, related_name='requests_requestedBy')
	adminApproved = models.ForeignKey(UserProfile, related_name='requests_adminApproved')
	chairApproves = models.ForeignKey(UserProfile, related_name='requests_chairApproves')

	class Meta:
		verbose_name_plural = 'Requests'


