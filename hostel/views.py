from .models import HostelAllotment, User
from .hostel_allotment_forms import HostelAllotmentForm
def hostel_allotment(request, pk):
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
    rooms = list(range(501, 551))
    return render(request, 'room_grid.html', {'rooms': rooms})


