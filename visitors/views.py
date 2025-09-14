from django.shortcuts import render, redirect
from .forms import VisitorRecordForm
from .models import VisitorRecord

def record_visitor(request):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('home')
    if request.method == 'POST':
        form = VisitorRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_success')
    else:
        form = VisitorRecordForm()
    return render(request, 'visitors/record_visitor.html', {'form': form})


from django.utils import timezone
from datetime import datetime

def visitor_success(request):
    return render(request, 'visitors/visitor_success.html')

def history(request):
    if hasattr(request.user, 'role') and request.user.role == 'student':
        return redirect('home')
    selected_date = request.GET.get('date')
    visitors = []
    if not selected_date:
        selected_date = timezone.localdate().strftime('%Y-%m-%d')
    try:
        date_obj = datetime.strptime(selected_date, "%Y-%m-%d")
        visitors = VisitorRecord.objects.filter(visit_time__date=date_obj.date()).order_by('visit_time')
    except Exception:
        visitors = []
    return render(request, 'visitors/visitor_history.html', {
        'visitors': visitors,
        'selected_date': selected_date,
    })

