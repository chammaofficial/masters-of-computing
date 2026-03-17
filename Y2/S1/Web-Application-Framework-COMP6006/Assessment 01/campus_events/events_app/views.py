from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from events_app.forms import EventForm
from events_app.models import Event, Category
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    queryResultSet = Event.objects.filter(start_datetime__gte=timezone.now(), is_approved=True).order_by('start_datetime')[:3]
    return render(request, 'index.html', {'upcoming_events': queryResultSet})

def event_list(request):
    queryResultSet = Event.objects.filter(start_datetime__gte=timezone.now(), is_approved=True).order_by('start_datetime')
    return render(request, 'event_list.html' ,{'events': queryResultSet})

def category_list(request):
    queryResultSet = Category.objects.all()
    return render(request, 'category_list.html',{'categories': queryResultSet})

def category_events(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    queryResultSet = Event.objects.filter(category_id=category_id, start_datetime__gte=timezone.now(), is_approved=True).order_by('start_datetime')
    return render(request, 'category_event_list.html' ,{'events': queryResultSet, 'category' : category})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id, is_approved=True)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    form = EventForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your event is submitted. It will appear as soon as approved.')
            return redirect('events')
        else:
            for error in form.errors.values():
                messages.error(request, error[0])
    return render(request, 'event_create.html', {'form': form})
