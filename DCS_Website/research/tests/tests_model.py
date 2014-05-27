from django.test import TestCase
from research.models import Lab, Field, Adviser 
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.
class LabModelTest(TestCase):
	"""Test for Lab section Models"""
	def create_lab(self,name='QWQQWWW',abbr='qwewqeqwe'):
		return Lab.objects.create(name=name,abbr=abbr)
	
	def test_lab_creation(self):
		lab = self.create_lab()
		self.assertTrue(isinstance(lab,Lab))
		self.assertEqual(lab.__str__(),lab.name)

# class FeildModelTest(TestCase):
# 	"""Test for Field section Models"""
# 	def create_lab(self,name='QWQQWWW',abbr='qwewqeqwe'):
# 		return Lab.objects.create(name=name,abbr=abbr)

# 	def create_field(self,lab_name='lab',field_name='field'):
# 		lab2 = self.create_lab('nye', 'nye')
# 		return Field.objects.create(lab2)
	
# 	def test_field_creation(self):
# 		field = self.create_field()
# 		self.assertTrue(isinstance(field,Field))
# 		self.assertEqual(field.__str__(),field.field_name)
