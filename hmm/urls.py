from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from strip.rss import LatestEntriesFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    # Views
    url(r'^$', 'strip.views.index'),
    url(r'^(?P<number>\d+)/$', 'strip.views.index'),
    # API
    (r'^api/strip/', include('strip.urls')),
    (r'^api/bonus/', include('bonus.urls')),
    # Feeds
    (r'^rss/', LatestEntriesFeed()),
)

urlpatterns += staticfiles_urlpatterns()
