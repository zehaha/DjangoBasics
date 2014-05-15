from django.template.loader import render_to_string
from django.test import TestCase, Client
from images.models import Image
from django.conf.urls import patterns, url

class ImageModelTest(TestCase):
	"""Test for image models"""
	def create_image(self,caption='asdasd',shown_in='asdasd'):
		return Image.objects.create(caption=caption,shown_in=shown_in)
	def test_image_creation(self):
		image = self.create_image()
		self.assertTrue(isinstance(image,Image))
		self.assertEqual(image.__str__(),(image.caption))
