from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.list_detail import object_list
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import Shout

def shout_list(request, notice = ""):
    """Shows all shouts"""
    
    if 'shout' in request.POST and request.POST['shout']:
         if request.POST['poster']:
             poster = request.POST['poster']
         else:
             poster = 'Anonymous'
             
         s = Shout(post_as = poster, content = request.POST['shout'])
         s.save()
         return HttpResponseRedirect(reverse('shouts.views.shout_list'))
    else:
         return object_list(request,
                            queryset = Shout.objects.all(),
                            template_object_name = 'shouts',
                            paginate_by=5,
                            extra_context = { 'notice' : notice }
		                    )