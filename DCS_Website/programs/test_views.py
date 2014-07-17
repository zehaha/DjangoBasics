from django.test import TestCase, Client

# Create your tests here.
class ProgramsTest(TestCase):
    """Unit tests for all the views of the programs app."""
    def setUp(self):
        self.client_stub = Client()

    def test_programs(self):
        response = self.client_stub.get('/programs/')
        self.assertEqual(response.status_code, 200)
