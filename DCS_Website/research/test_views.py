from django.test import TestCase, Client

class ResearchViewTest(TestCase):
    """Unit tests for all the views of the research app."""
    def setUp(self):
        self.client_stub = Client()

    def test_research(self):
        response = self.client_stub.get('/research/')
        self.assertEqual(response.status_code, 200)
