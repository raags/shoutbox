from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Shout

def shout_list(request, notice = ""):
	
	if 'shout' in request.POST and request.POST['shout']:
		s = Shout(post_as = request.POST['poster'], content = request.POST['shout'])
    		s.save()
		return  HttpResponseRedirect(reverse('shouts.views.shout_list'))
	
#		return render_to_response('shouts/shout_list.html', {
#		'notice': "add content",
#		}, context_instance=RequestContext(request))

	else:			
		"""Show all shouts"""
		return object_list(request, 
		queryset = Shout.objects.all(),
		template_object_name = 'shouts', 
		extra_context = {'notice': notice}
)

def shout_post(request):
	"""Post new shout"""
	return create_object(request,
	model = Shout,
	post_save_redirect = reverse("shout_list")
)
