from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from DCS_Website import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

"""Use a regular expression to request the object by its primary key and execute
the corresponding view when the object is found."""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DCS_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'DCS_Website.views.home', name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^announcements/', include('announcements.urls')),
    url(r'^about/', 'DCS_Website.views.about'),
    url(r'^people/', include('people.urls')),
    url(r'^programs/BS CS Curriculum/download', 'DCS_Website.views.download_BS_CS_Curriculum'),
    url(r'^programs/MS CS Curriculum/download', 'DCS_Website.views.download_MS_CS_Curriculum'),
    url(r'^programs/PhD CS Curriculum/download', 'DCS_Website.views.download_PhD_CS_Curriculum'),
    url(r'^contact/', 'DCS_Website.views.contact'),
    url(r'^programs/', 'DCS_Website.views.programs'),
    url(r'^affiliates/', 'DCS_Website.views.affiliates'),
    url(r'^research/', 'DCS_Website.views.research'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
