from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views
from home import views as myviews

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^home/add_reservation/$', myviews.add_request, name='add_request'),
    url(r'^home/request/$', myviews.request_detail, name='add_request'),
    url(r'^home/reservation_lists/$', myviews.reservation_list, name='add_request'),
)
