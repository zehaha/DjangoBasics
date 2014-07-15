from django.conf.urls import patterns, url
from affiliates import views

urlpatterns = patterns('',
    url(r'^$', views.affiliates)
)
