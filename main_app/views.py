from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Wedding, Event

# Create your views here.
def home(request):
    return render(request, 'home.html')

class WeddingList(ListView):
    model = Wedding

class WeddingDetail(DetailView):
    model = Wedding

class WeddingCreate(CreateView):
    model = Wedding
    fields = '__all__'

class WeddingDelete(DeleteView):
    model = Wedding
    success_url = '/weddings/'

class WeddingUpdate(UpdateView):
    model = Wedding
    fields = ['description']

class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event

class EventCreate(CreateView):
    model = Event
    fields = ['type', 'description', 'start_date_time', 'end_date_time', 'venue']

class EventDelete(DeleteView):
    model = Event
    success_url = '/weddings/'
