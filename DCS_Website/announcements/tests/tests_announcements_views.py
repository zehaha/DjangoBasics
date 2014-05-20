from django.test import TestCase
from announcements.models import Announcement
from announcements.views import announcement_details
from django.utils import timezone
from django.core.urlresolvers import reverse

class Event_Views_Test(TestCase):
	"""Test for announcement views"""
	def create_Announcement(self, title = "just a test", body = "test only"):
		return Announcement.objects.create(title = title, body = body , pub_date = timezone.now())
		
	def test_Announcement_list_view(self):
		announcement1 = self.create_Announcement()
		url = reverse("announcement_details", args = (announcement1.id,))
		resp = self.client.get(url)
		
		self.assertEqual(resp.status_code, 200)
		self.assertIn(announcement1.title, resp.content)