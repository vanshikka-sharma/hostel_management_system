from django.db import models
from inventory.models import Item

class Complaint(models.Model):
	CATEGORY_CHOICES = [
		('electric','Electrical'),
		('furniture','Furniture'),
		('Mess','Mess'),
		('medical','Medical'),
		('misc','Miscellaneous'),
	]
	name = models.CharField(max_length=100)
	room_no = models.CharField(max_length=20)
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='misc')
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} - {self.category} ({self.room_no})"
