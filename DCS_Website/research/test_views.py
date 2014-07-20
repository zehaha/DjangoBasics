from django.test import TestCase
from django.core.urlresolvers import reverse

class ResearchViewTest(TestCase):
    """Unit tests for all the views of the research app."""
    def setUp(self):
        pass

    def test_research(self):
        response = self.client.get(reverse('research'))
        self.assertEqual(response.status_code, 200)
