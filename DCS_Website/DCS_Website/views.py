import os
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.static import serve
from django.core.servers.basehttp import FileWrapper
from news.models import NewsArticle
from events.models import Event
from announcements.models import Announcement
from images.models import Image

# Create your views here.
def home(request):
    """Fetch the requested objects with the given primary keys from the database,
    creat context by assigning the objects to corresponding variables in the template,
    and render the page using the context and the template in the given directory.
    """
    latest_news_article_list = NewsArticle.objects.order_by('-pub_date')[:3]
    latest_event_list = Event.objects.order_by('-date')[:3]
    latest_announcement_list = Announcement.objects.order_by('-pub_date')[:3]
    carousel_images = Image.objects.order_by('-id').filter(models.Q(shown_in='c') | models.Q(shown_in='b'))[:6]
    context = {'latest_news_article_list' : latest_news_article_list,
    			'latest_event_list' : latest_event_list,
    			'latest_announcement_list' : latest_announcement_list,
    			'carousel_images' : carousel_images,
    			}
    return render(request, 'home/home.html', context)

def download_BS_CS_Curriculum(request):
    """Find the file in the given directory, use FileWrapper to split it into smaller increments,
    make the wrapper into an HTTP response, define response attributes, and return the response.
    """
    filename = 'media/programs/BS CS Curriculum.pdf'
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper)
    response['Content-Name'] = os.path.getsize(filename)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="BS CS Curriculum.pdf"'
    response['Content-Length'] = os.path.getsize(filename)
    return response


def download_MS_CS_Curriculum(request):
    filename = 'media/programs/MS CS Curriculum.pdf'
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper)
    response['Content-Name'] = os.path.getsize(filename)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="MS CS Curriculum.pdf"'
    response['Content-Length'] = os.path.getsize(filename)
    return response

def download_PhD_CS_Curriculum(request):
    filename = 'media/programs/PhD CS Curriculum.pdf'
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper)
    response['Content-Name'] = os.path.getsize(filename)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="PhD CS Curriculum.pdf"'
    response['Content-Length'] = os.path.getsize(filename)
    return response

def programs(request):
    return render(request, 'programs/programs.html')

def contact(request):
    return render(request, 'contact/contact.html')

def affiliates(request):
    return render(request, 'affiliates/affiliates.html')

def research(request):
    return render(request, 'research/research.html')

def about(request):
    gallery_images = Image.objects.order_by('-id').filter(models.Q(shown_in='g') | models.Q(shown_in='b'))[:6]
    context = {'gallery_images' : gallery_images,
                }
    return render(request, 'about/about.html', context)
