from django.test import TestCase

class PeopleViewTests(TestCase):
    def setUp(self):
        pass

    def test_view_people_route(self):
        response = self.client.get('/people/')
        self.assertEquals(response.status_code, 200)
