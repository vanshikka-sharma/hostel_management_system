from django.db import models
from django.conf import settings

class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class EventVote(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='votes')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_participating = models.BooleanField()
	voted_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('event', 'user')
