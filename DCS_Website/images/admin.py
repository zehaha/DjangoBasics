from django.contrib import admin
from images.models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	"""Model for the interface in the admin page.
	list_display is the list of attributes displayed
	list_filter is the list of the attributes the objects can be filtered by
	search_fields is the list of attributes that the system goes through when using the search bar
	"""
	list_display = ('caption', 'shown_in')
	list_filter = ['shown_in']
	search_fields = ['caption']
	
admin.site.register(Image, ImageAdmin)