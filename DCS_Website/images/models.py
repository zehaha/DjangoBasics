from django.db import models

STATUS_CHOICES = (
	('g', 'Gallery'),
	('c', 'Carousel'),
	('b', 'Both gallery and carousel'),
	('h', 'Hidden'),
)

# Create your models here.
class Image(models.Model):
	image = models.ImageField(upload_to='images/')
	caption = models.TextField()
	shown_in = models.CharField(max_length=1, choices=STATUS_CHOICES)
	def __str__(self):
		return self.caption