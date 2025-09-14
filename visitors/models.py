from django.db import models
from hostel.models import HostelAllotment

class VisitorRecord(models.Model):
	visitor_name = models.CharField(max_length=100)
	visitor_purpose = models.CharField(max_length=200)
	adhar_card_number = models.CharField(max_length=16)
	room_allotment = models.ForeignKey(HostelAllotment, on_delete=models.CASCADE, related_name='visitors')
	visit_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.visitor_name} ({self.room_allotment.room_number})"
