from django.test import TestCase

# Create your tests here.
class HomeViewTests(TestCase):
    """Unit tests for all the views of the home app."""
    def setUp(self):
        pass

    def test_home_default(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
