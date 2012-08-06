from django.contrib import admin
from shouts.models import Shout

class ShoutAdmin(admin.ModelAdmin):
	list_display = ('post_as', 'content', 'pub_date',)
	list_filter = ('pub_date',)
	date_hierarchy = 'pub_date'

admin.site.register(Shout, ShoutAdmin)
