from django.db import models

# Create your models here.
class Announcement(models.Model):
	"""Model for the announcement objects."""
	pub_date = models.DateTimeField('Date Published')
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=200)
	def __str__(self): 
		return self.title
