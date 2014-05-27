from django.contrib import admin
from affiliates.models import Affiliate

# Register your models here.

class AffiliateAdmin(admin.ModelAdmin):
	"""Model for the interface in the admin page.
	list_display is the list of attributes displayed
	list_filter is the list of the attributes the objects can be filtered by
	search_fields is the list of attributes that the system goes through when using the search bar
	"""
	list_display = ('link', 'name','logo','status', 'corporate_donor', 'description', 'contribution')
	list_filter = ['name']
	search_fields = ['name', 'status', 'corporate_donor']

admin.site.register(Affiliate, AffiliateAdmin)