from django.contrib import admin
from home.models import Rooms, Events, Schedules, Requests
# Register your models here.
admin.site.register(Rooms)
admin.site.register(Events)
admin.site.register(Schedules)
admin.site.register(Requests)