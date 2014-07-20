from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class ProgramsTest(TestCase):
    """Unit tests for all the views of the programs app."""
    def setUp(self):
        pass

    def test_programs(self):
        response = self.client.get(reverse('programs'))
        self.assertEqual(response.status_code, 200)
