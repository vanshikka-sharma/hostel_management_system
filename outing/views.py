from django.shortcuts import render, redirect
from .forms import OutingApplicationForm
from .models import OutingApplication
from django.contrib.auth.decorators import login_required
from .models import OutingApplication



def outing_list(request):
    outings = OutingApplication.objects.select_related('user', 'room_allotment').order_by('-applied_at')
    if request.method == 'POST':
        outing_id = request.POST.get('outing_id')
        action = request.POST.get('action')
        if outing_id and action in ['accept', 'reject']:
            try:
                outing = OutingApplication.objects.get(id=outing_id)
                outing.status = 'accepted' if action == 'accept' else 'rejected'
                outing.save()
            except OutingApplication.DoesNotExist:
                pass
        return redirect('outing_list')
    return render(request, 'outing/outing_list.html', {'outings': outings})

@login_required
def apply_outing(request):
    if request.method == 'POST':
        form = OutingApplicationForm(request.POST)
        if form.is_valid():
            outing = form.save(commit=False)
            outing.user = request.user
            outing.save()
            return redirect('outing_list')
    else:
        form = OutingApplicationForm()
    return render(request, 'outing/apply_outing.html', {'form': form})

def applyhistory(request):
    pass
