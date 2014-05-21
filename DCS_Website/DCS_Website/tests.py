from django.test import TestCase, Client
from django.template.loader import render_to_string
from DCS_Website.views import *

# Create your tests here.
class ViewTest(TestCase):
	"""Test for views of all pages"""
	def setUp(self):
		self.client_stub = Client()
	def test_view_home_route(self):
		response = self.client_stub.get('/')
		self.assertEquals(response.status_code, 200)
	def test_BSCS_Curriculum_Download_route(self):
		response = self.client_stub.get('/programs/BS CS Curriculum/download')
		self.assertEquals(response.status_code, 200)
	def test_MSCS_Curriculum_Download_route(self):
		response = self.client_stub.get('/programs/MS CS Curriculum/download')
		self.assertEquals(response.status_code, 200)
	def test_PhDCS_Curriculum_Download_route(self):
		response = self.client_stub.get('/programs/PhD CS Curriculum/download')
		self.assertEquals(response.status_code, 200)
	def test_programs_route(self):
		response = self.client_stub.get('/programs/')
		self.assertEquals(response.status_code, 200)
	def test_contact_route(self):
		response = self.client_stub.get('/contact/')
		self.assertEquals(response.status_code, 200)
	def test_affiliates_route(self):
		response = self.client_stub.get('/affiliates/')
		self.assertEquals(response.status_code, 200)
	def test_about_route(self):
		response = self.client_stub.get('/about/')
		self.assertEquals(response.status_code, 200)
	def test_research_route(self):
		response = self.client_stub.get('/research/')
		self.assertEquals(response.status_code, 200)
