from django.contrib import admin
from research.models import Lab, Field, Adviser

"""Models for the interface in the admin page.
list_display is the list of attributes displayed
list_filter is the list of the attributes the objects can be filtered by
search_fields is the list of attributes that the system goes through when using the search bar
"""
class LabAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbr','head')
	list_filter = ['name']
	search_fields = ['name']

class FieldAdmin(admin.ModelAdmin):
	list_display = ('field_name','lab_name')
	list_filter = ['lab_name']
	search_fields = ['lab_name']
	
class AdviserAdmin(admin.ModelAdmin):
	list_display = ('adviser_name','lab_name')
	list_filter = ['lab_name']
	search_fields = ['adviser_name']

admin.site.register(Lab, LabAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Adviser, AdviserAdmin)