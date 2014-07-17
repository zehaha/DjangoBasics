from django.test import TestCase, Client

class AffiliateViewTest(TestCase):
    """Unit tests for all the views of the affiliates app."""
    def setUp(self):
        self.client_stub = Client()

    def test_affiliates(self):
        response = self.client_stub.get('/affiliates/')
        self.assertEquals(response.status_code, 200)
