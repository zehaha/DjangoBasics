from django.contrib import admin
from images.models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display = ('caption', 'shown_in')
	list_filter = ['shown_in']
	search_fields = ['caption']
	
admin.site.register(Image, ImageAdmin)