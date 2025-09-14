from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Student, Attendance

def mark_attendance(request):
    students = Student.objects.all()
    if request.method == "POST":
        for student in students:
            status = request.POST.get(f'status_{student.id}')
            remarks = request.POST.get(f'remarks_{student.id}')
            Attendance.objects.create(
                student=student,
                date=timezone.now().date(),
                status=status,
                remarks=remarks
            )
        return redirect('view_attendance')
    return render(request, 'attendence/templates/mark_attendence.html', {'students': students})


def view_attendance(request):
    today = timezone.now().date()
    records = Attendance.objects.filter(date=today)

    total_students = records.count()
    present_count = records.filter(status='P').count()
    absent_count = records.filter(status='A').count()

    return render(request, 'attendence/templates/view_attendence.html', {
        'records': records,
        'total': total_students,
        'present': present_count,
        'absent': absent_count,
        'date': today
    })

