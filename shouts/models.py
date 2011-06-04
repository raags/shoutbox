from django.db import models

class Shout(models.Model):
	"""Model to save our shouts"""

	post_as = models.CharField(max_length=30)  
	content = models.TextField(max_length=255)
	# automatically add timestamps when object is created
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.post_as
