from django.test import TestCase, Client

# Create your tests here.
class HomeTest(TestCase):
    """Unit tests for all the views of the home app."""
    def setUp(self):
        self.client_stub = Client()

    def test_home_default(self):
        response = self.client_stub.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home(self):
        response = self.client_stub.get('/home/')
        self.assertEquals(response.status_code, 200)
