from django.shortcuts import render
from announcements.models import Announcement

# Create your views here.
def announcement_details(request, pk):
	"""Fetch the requested object with the given primary key from the database,
	create context by assigning the object to a corresponding variable in the template,
	and render the page using the context and the template in the given directory.
	"""
	announcement = Announcement.objects.get(id=pk)
	context = {'announcement' : announcement}
	return render(request, 'announcements/announcements.html', context)