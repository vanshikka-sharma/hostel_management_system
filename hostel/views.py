def room_list(request):
    # Get all room allotments, group by room number
    from collections import defaultdict
    rooms = defaultdict(list)
    for allotment in HostelAllotment.objects.select_related('user').order_by('room_number'):
        rooms[allotment.room_number].append(allotment)
    room_data = []
    for room_number, allotments in rooms.items():
        users = [{'name': a.user.name, 'phone': a.user.phone_number} for a in allotments]
        room_data.append({'room_number': room_number, 'users': users})
    room_data.sort(key=lambda x: x['room_number'])
    return render(request, 'room_list.html', {'room_data': room_data})
from .models import HostelAllotment, User
from .hostel_allotment_forms import HostelAllotmentForm
def hostel_allotment(request, pk):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access the hostel allotment page.')
        return redirect('home')
    room_number = pk
    if request.method == 'POST':
        form = HostelAllotmentForm(request.POST)
        if form.is_valid():
            allotment = form.save(commit=False)
            allotment.room_number = room_number
            # Automatically set total_payable
            allotment.total_payable = form.cleaned_data['security_fees'] + form.cleaned_data['allotment_fees']
            allotment.save()
            messages.success(request, f'Hostel room {room_number} allotted to {allotment.user.name}.')
            return redirect('hostel_allotment', pk=room_number)
    else:
        form = HostelAllotmentForm()
    return render(request, 'hostel_allotment.html', {'form': form, 'room_number': room_number})
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access the registration page.')
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('register')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})



def room_allotment(request):
    user = request.user
    if user.is_authenticated and getattr(user, 'role', None) == 'student':
        messages.info(request, 'Students cannot access the room allotment page.')
        return redirect('home')
    rooms = list(range(501, 551))
    return render(request, 'room_grid.html', {'rooms': rooms})


