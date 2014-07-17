from django.test import TestCase

# Create your tests here.
class AboutViewTest(TestCase):
    """Unit tests for all the views of the about app."""
    def setUp(self):
        pass

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
