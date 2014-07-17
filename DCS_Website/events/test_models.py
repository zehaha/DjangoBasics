from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from events.models import Event

# Create your tests here.
class EventsModelTests(TestCase):
    """Unit tests for all models of the events app."""
    def setUp(self):
        pass

    def create_Event(self, description = "test only"):
        return Event.objects.create(description=description, date=timezone.now())

    def test_Event_creation(self):
        event1 = self.create_Event()
        self.assertTrue(isinstance(event1, Event))
        self.assertEqual(event1.__str__(), event1.description)
