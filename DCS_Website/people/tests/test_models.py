from django.template.loader import render_to_string
from django.test import TestCase, Client
from people.models import Faculty, Student, Staff
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from people.views import *

class StudentModelTest(TestCase):
	"""Test for Students section Models"""
	def create_student(self,org_name='InterSoc',description='asdsqad'):
		return Student.objects.create(org_name=org_name,description=description)
	
	def test_student_creation(self):
		student = self.create_student()
		self.assertTrue(isinstance(student,Student))
		self.assertEqual(student.__str__(),student.org_name)

class FacultyModelTest(TestCase):
	"""Test for Faculty Models"""
	def create_faculty(self,first_name='Paul',middle_name='V',last_name='Sacedor',position='Instructor'):
		return Faculty.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,position=position)
	
	def test_faculty_creation(self):
		faculty = self.create_faculty()
		self.assertTrue(isinstance(faculty,Faculty))
		self.assertEqual(faculty.__str__(), (faculty.last_name + ", " + faculty.first_name + " " + faculty.middle_name))

class StaffModelTest(TestCase):
	"""Test for Staff Models"""
	def create_staff(self,first_name='Paul',middle_name='V',last_name='Sacedor',position='Instructor'):
		return Staff.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,position=position)

	def test_staff_creation(self):
		staff = self.create_staff()
		self.assertTrue(isinstance(staff,Staff))
		self.assertEqual(staff.__str__(), (staff.last_name + ", " + staff.first_name + " " + staff.middle_name))

class PeopleViewTest(TestCase):
	def setUp(self):
		self.client_stub = Client()
	def test_view_people_route(self):
		response = self.client_stub.get('/people/')
		self.assertEquals(response.status_code, 200)