from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class AboutViewTest(TestCase):
    """Unit tests for all the views of the about app."""
    def setUp(self):
        pass

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
