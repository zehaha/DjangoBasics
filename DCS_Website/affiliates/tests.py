from django.test import TestCase
from affiliates.models import Affiliate
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.
class AffiliatesModelTest(TestCase):
	"""Test for Affiliates Models"""
	def create_affiliate(self,name='asd', status='True', corporate_donor = 'True'):
		return Affiliate.objects.create(name=name, status = status, corporate_donor = corporate_donor)
	
	def test_aff_creation(self):
		aff = self.create_affiliate()
		self.assertTrue(isinstance(aff,Affiliate))
		self.assertEqual(aff.__str__(),aff.name)

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
