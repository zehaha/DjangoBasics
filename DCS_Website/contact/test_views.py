from django.test import TestCase, Client

# Create your tests here.
class ContactTest(TestCase):
    """Unit tests for all the views of the contact app."""
    def setUp(self):
        self.client_stub = Client()

    def test_contact(self):
        response = self.client_stub.get('/contact/')
        self.assertEqual(response.status_code, 200)
