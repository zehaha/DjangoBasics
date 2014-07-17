from django.test import TestCase

class ResearchViewTest(TestCase):
    """Unit tests for all the views of the research app."""
    def setUp(self):
        pass

    def test_research(self):
        response = self.client.get('/research/')
        self.assertEqual(response.status_code, 200)
