from django.test import TestCase
from affiliates.models import Affiliate

# Create your tests here.
class AffiliatesModelTest(TestCase):
    """Unit tests for all the models of the affiliates app."""
    def create_affiliate(self,name='asd', status='True', corporate_donor = 'True'):
        return Affiliate.objects.create(name=name, status = status, corporate_donor = corporate_donor)

    def test_aff_creation(self):
        aff = self.create_affiliate()
        self.assertTrue(isinstance(aff,Affiliate))
        self.assertEqual(aff.__str__(),aff.name)
