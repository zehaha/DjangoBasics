from django.test import TestCase
from django.utils import timezone
from announcements.models import Announcement

# Create your tests here.
class AnnouncementsModelTests(TestCase):
    """Test for Announcements models"""
    def setUp(self):
        pass

    def create_Announcement(self, title = "just a test", body = "test only"):
        return Announcement.objects.create(title = title, body = body , pub_date = timezone.now())

    def test_Announcement_creation(self):
        announcement1 = self.create_Announcement()
        self.assertTrue(isinstance(announcement1, Announcement))
        self.assertEqual(announcement1.__str__(), announcement1.title)
