from django.conf.urls.defaults import *

urlpatterns = patterns('shouts.views',

	url(r'^$','shout_list', name='shout_list'),
)
