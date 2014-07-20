from django.test import TestCase
from django.core.urlresolvers import reverse

class PeopleViewTests(TestCase):
    def setUp(self):
        pass

    def test_view_people_route(self):
        response = self.client.get(reverse('people'))
        self.assertEquals(response.status_code, 200)
