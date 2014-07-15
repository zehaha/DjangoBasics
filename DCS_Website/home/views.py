from django.shortcuts import render

from events.models import Event
from announcements.models import Announcement
from images.models import Image

from django.db import models
# Create your views here.

def home(request):
    """Fetch the requested objects with the given primary keys from the database,
    creat context by assigning the objects to corresponding variables in the template,
    and render the page using the context and the template in the given directory.
    """
    latest_event_list = Event.objects.order_by('-date')[:3]
    latest_announcement_list = Announcement.objects.order_by('-pub_date')[:3]
    carousel_images = Image.objects.order_by('-id').filter(models.Q(shown_in='c') | models.Q(shown_in='b'))[:6]
    context = {'latest_event_list' : latest_event_list,
                'latest_announcement_list' : latest_announcement_list,
                'carousel_images' : carousel_images,
                }
    return render(request, 'home/home.html', context)
