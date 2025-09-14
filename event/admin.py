from django.contrib import admin
from .models import Event, EventVote

admin.site.register(Event)
admin.site.register(EventVote)
