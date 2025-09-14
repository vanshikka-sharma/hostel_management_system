from django.shortcuts import render, redirect
from hostel.models import User
from .models import Parcel
from django.contrib import messages

# Create your views here.
def base(request):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('parcel:history')
    # Show all students with room numbers
    students = User.objects.filter(role='student').values('id', 'name', 'hostel_allotments__room_number')
    # Remove duplicates and get latest room number
    student_list = []
    seen = set()
    for s in students:
        if s['id'] not in seen and s['hostel_allotments__room_number']:
            student_list.append({'id': s['id'], 'name': s['name'], 'room_number': s['hostel_allotments__room_number']})
            seen.add(s['id'])
    return render(request, 'parcel_notify.html', {'students': student_list})

def history(request):
    parcels = Parcel.objects.select_related('user').order_by('-received_at')
    return render(request, 'parcel_history.html', {'parcels': parcels})

def send_parcel(request):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('parcel:history')
    if request.method == 'POST':
        ids = request.POST.getlist('student_ids')
        for user_id in ids:
            user = User.objects.get(id=user_id)
            room_number = user.hostel_allotments.last().room_number if user.hostel_allotments.exists() else None
            Parcel.objects.create(user=user, room_number=room_number, notified=True)
            # Here you can add SMS/email logic
        messages.success(request, 'Parcel notifications sent!')
        return redirect('parcel:base')
    return redirect('parcel:base')
