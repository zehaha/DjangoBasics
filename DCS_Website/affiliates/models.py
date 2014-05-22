from django.db import models

# Create your models here.

class Affiliate(models.Model):
	link = models.URLField()
	name = models.CharField(max_length=256)
	logo = models.ImageField(upload_to='aff_logos/')
	status = models.BooleanField()
	corporate_donor = models.BooleanField()
	description = models.TextField(blank = True)
	contribution = models.TextField(blank = True)
	def __unicode__(self):
		return self.name