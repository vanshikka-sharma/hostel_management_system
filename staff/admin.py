# staff/admin.py
from django.contrib import admin
from .models import StaffMember, Shift, ShiftAssignment, SalaryRecord

@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','staff_type','phone','email','date_of_joining')
    list_filter = ('staff_type',)
    search_fields = ('first_name','last_name','phone','email')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name','start_time','end_time')

@admin.register(ShiftAssignment)
class ShiftAssignmentAdmin(admin.ModelAdmin):
    list_display = ('staff','shift','date','created_at')
    list_filter = ('date','shift')

@admin.register(SalaryRecord)
class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ('staff','year','month','base_salary','final_salary')
    list_filter = ('year','month','staff')

