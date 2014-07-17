from django.test import TestCase
from events.models import Event
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.
class EventsViewTests(TestCase):
    """Unit tests for all the views of the event app."""
    def setUp(self):
        pass

    def create_Event(self, description = "test only"):
        return Event.objects.create(description=description, date=timezone.now())

    def test_Event_view(self):
        eTest = self.create_Event()
        url =reverse('event_details', args = (eTest.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(eTest.description, response.content)
        self.assertContains(response, eTest.description , status_code = 200)
