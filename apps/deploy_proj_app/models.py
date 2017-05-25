from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
	location = models.CharField(max_length=38) #ex: San Jose, Seattle
	state = models.CharField(max_length=38) #ex: CA, WA
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "id: " + str(self.id) + ", location: " + self.location + ", state: " + self.state