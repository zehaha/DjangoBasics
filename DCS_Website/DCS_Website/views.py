from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from news.models import NewsArticle
from events.models import Event
from announcements.models import Announcement
from people.models import Faculty, Staff, Student
from images.models import Image

# Create your views here.
def home(request):
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

def about(request):
    gallery_images = Image.objects.order_by('-id').filter(models.Q(shown_in='g') | models.Q(shown_in='b'))[:6]
    context = {'gallery_images' : gallery_images,
                }
    return render(request, 'about/about.html', context)

def pipz(request):
    faculty_list = Faculty.objects.order_by('-position')
    student_list = Student.objects.order_by('-org_name')
    staff_list = Staff.objects.order_by('-last_name')
    
    faculty_assistant_list = Faculty.objects.filter(position__startswith='Assistant').order_by('last_name')
    faculty_associate_list = Faculty.objects.filter(position__startswith='Associate').order_by('last_name')
    faculty_instructor_list = Faculty.objects.filter(position__startswith='Instructor').order_by('last_name')
    
    pipz_context = {'faculty_list' : faculty_list,
                    'student_list' : student_list,
            'staff_list' : staff_list,
            'faculty_instructor_list' : faculty_instructor_list,
            'faculty_assistant_list' : faculty_assistant_list,
            'faculty_associate_list' : faculty_associate_list}
    return render(request, 'home/people.html', pipz_context)