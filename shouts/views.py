from django.views.generic.list_detail import object_list
from models import Shout

def shout_list(request, notice = ""):
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
