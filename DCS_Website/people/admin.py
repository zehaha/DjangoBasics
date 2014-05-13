from django.contrib import admin
from people.models import Faculty, Student, Staff

"""Models for the interface in the admin page.
list_display is the list of attributes displayed
list_filter is the list of the attributes the objects can be filtered by
search_fields is the list of attributes that the system goes through when using the search bar
"""
class FacultyAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'middle_name','last_name','position','email', 'photo')
	list_filter = ['position']
	search_fields = ['first_name', 'last_name','position']

class StudentAdmin(admin.ModelAdmin):
	list_display = ('org_name', 'description','logo')
	list_filter = ['org_name']
	search_fields = ['org_name']
	
class StaffAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'middle_name', 'last_name','position', 'room')
	list_filter = ['position']
	search_fields = ['first_name', 'last_name', 'position', 'room']

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)