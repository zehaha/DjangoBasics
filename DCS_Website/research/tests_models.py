from django.test import TestCase
from research.models import Lab

# Create your tests here.
class ResearchModelTest(TestCase):
    """Unit test for all the models of the research app."""
    def setUp(self):
        pass

    def create_lab(self,name='QWQQWWW',abbr='qwewqeqwe'):
        return Lab.objects.create(name=name,abbr=abbr)

    def test_lab_creation(self):
        lab = self.create_lab()
        self.assertTrue(isinstance(lab,Lab))
        self.assertEqual(lab.__str__(),lab.name)
