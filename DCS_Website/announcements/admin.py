from django.contrib import admin
from announcements.models import Announcement

# Register your models here.
class AnnouncementAdmin(admin.ModelAdmin):
	"""Model for the interface in the admin page.
	list_display is the list of attributes displayed
	list_filter is the list of the attributes the objects can be filtered by
	search_fields is the list of attributes that the system goes through when using the search bar
	"""
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Announcement, AnnouncementAdmin)