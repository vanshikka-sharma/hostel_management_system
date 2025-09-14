from django.db import models

class StaffMember(models.Model):
    ROLE_CHOICES = [
        ('Security', 'Security'),
        ('Mess', 'Mess'),
        ('Management', 'Management'),
        ('Cleaning', 'Cleaning'),
    ]

    SHIFT_CHOICES = [
        ('Day', 'Day'),
        ('Night', 'Night'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name



