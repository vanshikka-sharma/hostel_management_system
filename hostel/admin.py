from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HostelAllotment
@admin.register(HostelAllotment)
class HostelAllotmentAdmin(admin.ModelAdmin):
	list_display = ('room_number', 'user', 'security_fees', 'allotment_fees', 'total_payable', 'created_at')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
	model = User
	list_display = ('username', 'name', 'email', 'role', 'college_roll_no')
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('name', 'adhaar_card_number', 'phone_number', 'parents_name', 'parents_phone_number', 'city', 'state', 'alternate_phone_number', 'college_roll_no', 'branch', 'course', 'role')}),
	)
