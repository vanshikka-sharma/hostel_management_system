from django.shortcuts import render, redirect
from .models import Notice
from django.utils import timezone
from datetime import timedelta

def base(request):
    # Delete notices older than 3 months
    three_months_ago = timezone.now() - timedelta(days=90)
    from .models import Notice
    Notice.objects.filter(created_at__lt=three_months_ago).delete()
    notices = Notice.objects.order_by('-created_at')
    return render(request, 'notice_base.html', {'notices': notices})

def add(request):
    if request.method == 'POST':
        text = request.POST.get('notice_text', '').strip()
        if text:
            Notice.objects.create(text=text, created_at=timezone.now())
            return redirect('notice:base')
    return render(request, 'notice_add.html')

