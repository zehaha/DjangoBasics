from django.test import TestCase
from events.models import Event
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.
class Event_Models_Test(TestCase):
	"""Test for Event models"""
	def create_Event(self, description = "test only"):
		return Event.objects.create(description=description, date=timezone.now())
	def test_Event_creation(self):
		event1 = self.create_Event()
		self.assertTrue(isinstance(event1, Event))
		self.assertEqual(event1.__str__(), event1.description)
