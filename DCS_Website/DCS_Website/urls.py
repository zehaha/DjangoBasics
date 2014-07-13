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
    url(r'^events/', include('events.urls')),
    url(r'^announcements/', include('announcements.urls')),
    url(r'^about/', 'DCS_Website.views.about'),
    url(r'^people/', include('people.urls')),
    url(r'^programs/', include('programs.urls')),
    url(r'^contact/', 'DCS_Website.views.contact'),
    url(r'^affiliates/', 'DCS_Website.views.affiliates'),
    url(r'^research/', include('research.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
