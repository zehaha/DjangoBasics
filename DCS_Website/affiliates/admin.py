from django.contrib import admin
from affiliates.models import Affiliate

# Register your models here.

class AffiliateAdmin(admin.ModelAdmin):
	list_display = ('link', 'name','logo','status', 'corporate_donor', 'description', 'contribution')
	list_filter = ['name']
	search_fields = ['name', 'status', 'corporate_donor']

admin.site.register(Affiliate, AffiliateAdmin)