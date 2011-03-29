from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^shoutbox/$', include('shouts.urls')),
    (r'^admin/', include(admin.site.urls)),
)
