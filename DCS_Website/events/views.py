from django.shortcuts import render
from events.models import Event

# Create your views here.
def event_details(request, pk):
	"""Fetch the requested object with the given primary key from the database,
	create context by assigning the object to a corresponding variable in the template,
	and render the page using the context and the template in the given directory.
	"""
	event = Event.objects.get(id=pk)
	context = {'event' : event}
	return render(request, 'events/events.html', context)