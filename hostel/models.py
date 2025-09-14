from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model for role-based registration
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('management', 'Management'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    adhaar_card_number = models.CharField(max_length=16, unique=True)
    phone_number = models.CharField(max_length=10)
    parents_name = models.CharField(max_length=100)
    parents_phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    alternate_phone_number = models.CharField(max_length=10, blank=True, null=True)
    college_roll_no = models.CharField(max_length=50, unique=True)
    branch = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.role})"

