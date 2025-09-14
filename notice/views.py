from django.shortcuts import render, redirect
from .models import Notice
from django.utils import timezone

def base(request):
    notices = Notice.objects.order_by('-created_at')
    return render(request, 'notice_base.html', {'notices': notices})

def add(request):
    if request.method == 'POST':
        text = request.POST.get('notice_text', '').strip()
        if text:
            Notice.objects.create(text=text, created_at=timezone.now())
            return redirect('notice:base')
    return render(request, 'notice_add.html')

