from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event, EventVote

def event_list(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'event/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        Event.objects.create(title=title, description=description, date=date, time=time)
        return redirect('event_list')
    return render(request, 'event/event_create.html')

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    votes_yes = event.votes.filter(is_participating=True).count()
    votes_no = event.votes.filter(is_participating=False).count()
    user_vote = None
    all_votes = event.votes.select_related('user').all()
    if request.user.is_authenticated:
        user_vote = event.votes.filter(user=request.user).first()
    return render(request, 'event/event_detail.html', {
        'event': event,
        'votes_yes': votes_yes,
        'votes_no': votes_no,
        'user_vote': user_vote,
        'all_votes': all_votes
    })

@login_required
def event_vote(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        is_participating = request.POST.get('is_participating') == 'yes'
        vote, created = EventVote.objects.update_or_create(
            event=event,
            user=request.user,
            defaults={'is_participating': is_participating, 'voted_at': timezone.now()}
        )
        return redirect('event_detail', event_id=event.id)
    return redirect('event_detail', event_id=event.id)
