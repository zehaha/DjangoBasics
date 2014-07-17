from django.test import TestCase

# Create your tests here.
class ProgramsTest(TestCase):
    """Unit tests for all the views of the programs app."""
    def setUp(self):
        pass

    def test_programs(self):
        response = self.client.get('/programs/')
        self.assertEqual(response.status_code, 200)
