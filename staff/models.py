# staff/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone
import calendar

class StaffMember(models.Model):
    COOK = 'cook'
    CLEANER = 'cleaner'
    MANAGEMENT = 'management'
    SECURITY = 'security'
    STAFF_TYPE_CHOICES = [
        (COOK, 'Cook'),
        (CLEANER, 'Cleaner'),
        (MANAGEMENT, 'Management'),
        (SECURITY, 'Security'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
    date_of_joining = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_absolute_url(self):
        return reverse('staff:base')

class Shift(models.Model):
    """
    A shift template (like Morning, Evening, Night) with start/end times.
    """
    name = models.CharField(max_length=80)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"

class ShiftAssignment(models.Model):
    """
    Assign one or many staff to a Shift on a specific date.
    """
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='assignments')
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE, related_name='shift_assignments')
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('shift', 'staff', 'date')
        ordering = ['-date', 'shift__start_time']

    def __str__(self):
        return f"{self.staff} - {self.shift.name} on {self.date}"

class SalaryRecord(models.Model):
    """
    Salary record for each staff member, per month and year.
    """
    staff = models.ForeignKey(StaffMember, on_delete=models.CASCADE, related_name='salaries')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField(choices=[(i, calendar.month_name[i]) for i in range(1,13)])
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    holidays = models.PositiveIntegerField(default=0, help_text="Paid holidays in this month")
    off_days = models.PositiveIntegerField(default=0, help_text="Unpaid off days in this month")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('staff', 'year', 'month')
        ordering = ['-year', '-month']

    def __str__(self):
        return f"{self.staff} - {calendar.month_name[self.month]} {self.year}"

    @property
    def gross_salary(self):
        return self.base_salary + self.allowances

    @property
    def final_salary(self):
        # simple calc: subtract deductions and unpaid off-days (pro-rate by month days)
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        per_day = (self.base_salary) / days_in_month if days_in_month else 0
        off_day_deduction = per_day * self.off_days
        return (self.gross_salary - self.deductions - off_day_deduction)

