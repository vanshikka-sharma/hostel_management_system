from django.db import models
from django.contrib.auth import get_user_model
from hostel.models import HostelAllotment

class OutingApplication(models.Model):
	STATUS_CHOICES = (
		('pending', 'Pending'),
		('accepted', 'Accepted'),
		('rejected', 'Rejected'),
	)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	room_allotment = models.ForeignKey(HostelAllotment, on_delete=models.CASCADE)
	outing_date = models.DateField()
	purpose = models.CharField(max_length=200)
	applied_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

	def __str__(self):
		return f"{self.user.name} - {self.outing_date} ({self.status})"
