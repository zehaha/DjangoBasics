from django.test import TestCase, Client

# Create your tests here.
class AboutViewTest(TestCase):
    """Unit tests for all the views of the about app."""
    def setUp(self):
        self.client_stub = Client()

    def test_about(self):
        response = self.client_stub.get('/about/')
        self.assertEquals(response.status_code, 200)
