from django.shortcuts import render, redirect
from .models import Attendance
from hostel.models import User
from django import forms
from datetime import date as dt_date

class AttendanceDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

def attendance_list(request):
    date = request.GET.get('date')
    if not date:
        date = dt_date.today().isoformat()
    attendances = Attendance.objects.filter(date=date).select_related('user')
    form = AttendanceDateForm(initial={'date': date})
    # Prepare attendance_records for template
    attendance_records = []
    for attendance in attendances:
        attendance_records.append({
            'student': attendance.user,
            'present': attendance.present
        })
    return render(request, 'attendance_list.html', {
        'form': form,
        'attendance_records': attendance_records,
        'date': date,
    })

def mark_attendance(request):
    from datetime import date as dt_date
    today = dt_date.today()
    if hasattr(request.user, 'role') and request.user.role == 'management':
        # Management can only mark attendance for today
        if request.method == 'POST':
            date = request.POST.get('date')
            if date != today.isoformat():
                # Redirect or show previous attendance
                return redirect(f'/attendence/?date={date}')
            for user in User.objects.filter(role='student'):
                present = request.POST.get(f'present_{user.id}') == 'on'
                Attendance.objects.update_or_create(
                    user=user, date=date,
                    defaults={'present': present}
                )
            return redirect(f'/attendence/?date={date}')
        else:
            form = AttendanceDateForm(initial={'date': today})
            students = User.objects.filter(role='student')
            return render(request, 'mark_attendance.html', {
                'form': form,
                'students': students,
                'restrict_date': True,
            })
    else:
        # Other users (not management) can mark attendance as before
        if request.method == 'POST':
            date = request.POST.get('date')
            for user in User.objects.filter(role='student'):
                present = request.POST.get(f'present_{user.id}') == 'on'
                Attendance.objects.update_or_create(
                    user=user, date=date,
                    defaults={'present': present}
                )
            return redirect(f'/attendence/?date={date}')
        else:
            form = AttendanceDateForm()
            students = User.objects.filter(role='student')
            return render(request, 'mark_attendance.html', {
                'form': form,
                'students': students,
            })

def attendance_all(request):
    all_attendance = Attendance.objects.select_related('user').order_by('-date')
    return render(request, 'attendance_all.html', {
        'all_attendance': all_attendance,
    })


