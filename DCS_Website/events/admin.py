from django.contrib import admin
from events.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	"""Model for the interface in the admin page.
	list_display is the list of attributes displayed
	list_filter is the list of the attributes the objects can be filtered by
	search_fields is the list of attributes that the system goes through when using the search bar
	"""
	list_display = ('description', 'date')
	list_filter = ['date']
	search_fields = ['description']
	
admin.site.register(Event, EventAdmin)