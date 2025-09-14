from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # ya apne dashboard page ka naam
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


