from django.shortcuts import render, redirect
from .models import Complaint

def complaint_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        category = request.POST.get('category')
        description = request.POST.get('description')
        Complaint.objects.create(name=name, room_no=room_no, category=category, description=description)
        return redirect('complaint_status')
    return render(request, 'complaint/complaint_form.html')

def complaint_status(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'complaint/complaint_status.html', {'complaints': complaints})