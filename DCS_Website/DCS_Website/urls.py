from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from DCS_Website import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DCS_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'DCS_Website.views.home', name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^announcements/', include('announcements.urls')),
    url(r'^index/people/', 'DCS_Website.views.pipz', name='people'),
    url(r'^people/', include('people.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
