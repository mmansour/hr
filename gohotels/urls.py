from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from mezzanine.core.views import direct_to_template
admin.autodiscover()

urlpatterns = patterns('gohotels.views',
    url("^$", "home", name="home"),
    (r'^(?P<pageslug>[\w-]+)-(?P<hotelid>.*)/$', 'detail'),
)
  