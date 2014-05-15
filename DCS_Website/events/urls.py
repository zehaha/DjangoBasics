from django.conf.urls import patterns, url
from events import views

"""Use a regular expression to request the object by its primary key and execute
the corresponding view when the object is found."""
urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.event_details, name='event_details'),
)
