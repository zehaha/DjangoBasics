from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class ContactViewTests(TestCase):
    """Unit tests for all the views of the contact app."""
    def setUp(self):
        pass

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
