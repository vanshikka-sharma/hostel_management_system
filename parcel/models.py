from django.db import models
from hostel.models import User

# Create your models here.

class Parcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parcels')
    room_number = models.IntegerField()
    received_at = models.DateTimeField(auto_now_add=True)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"Parcel for {self.user.name} (Room {self.room_number})"
