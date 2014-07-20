from django.test import TestCase
from django.core.urlresolvers import reverse

class AffiliatesViewTest(TestCase):
    """Unit tests for all the views of the affiliates app."""
    def setUp(self):
        pass

    def test_affiliates(self):
        response = self.client.get(reverse('affiliates'))
        self.assertEquals(response.status_code, 200)
