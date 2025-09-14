from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.room_no})"


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('LV', 'On Leave'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.get_status_display()}"
