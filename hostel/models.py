from django.contrib.auth.models import AbstractUser
from django.db import models

# Extend Django's User model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('management', 'Management'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    parents_phone_no = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=15)
    college_roll_no = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.user.role})"

