from django.test import TestCase
from images.models import Image

class ImagesModelTests(TestCase):
    """Test for image models"""
    def setUp(self):
        pass

    def create_image(self,caption='asdasd',shown_in='asdasd'):
        return Image.objects.create(caption=caption,shown_in=shown_in)

    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image,Image))
        self.assertEqual(image.__str__(),(image.caption))
