from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def navbar(request):
    return render(request, 'navbar.html')

def login_view(request):
    """Handles user login."""
    if request.method == 'POST':
        # This is where you would process the form data from your HTML
        # In a real app, you would use a Django form and check for a valid user
        # For this example, we'll just print to the console
        print(f"Login attempt for user: {request.POST.get('username')}")
        return redirect('dashboard')  # Redirect to a dashboard on success
    return render(request, 'login.html') # The HTML file you provided

def logout_view(request):
    """Handles user logout."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def home(request):
    return render(request, 'home.html')



