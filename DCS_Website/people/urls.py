from django.conf.urls import patterns, url

from people import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/faculty_details/$', views.faculty_details, name='faculty_details'),
	url(r'^(?P<pk>\d+)/student_details/$', views.student_details, name='student_details'),
	url(r'^(?P<pk>\d+)/staff_details/$', views.staff_details, name='staff_details'),
)
