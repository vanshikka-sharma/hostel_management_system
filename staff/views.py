from django.shortcuts import render, redirect, get_object_or_404
from .models import StaffMember
from .forms import StaffForm

def staff_home(request):
    security_staff = StaffMember.objects.filter(role='Security')
    mess_staff = StaffMember.objects.filter(role='Mess')
    management_staff = StaffMember.objects.filter(role='Management')
    cleaning_staff = StaffMember.objects.filter(role='Cleaning')
    return render(request, 'staff.html', {
        'security_staff': security_staff,
        'mess_staff': mess_staff,
        'management_staff': management_staff,
        'cleaning_staff': cleaning_staff,
    })

def add_member(request):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('staff_home')
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_home')
    else:
        form = StaffForm()
    return render(request, 'add_members.html', {'form': form})

def shift_member(request, pk):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('staff_home')
    staff = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_home')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'shift_members.html', {'form': form, 'staff': staff})




