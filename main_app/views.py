from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse

from .models import Wedding, Event
from .forms import EventForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def weddings_detail(request, wedding_id):
    wedding = Wedding.objects.get(id=wedding_id)
    event_form = EventForm()
    return render(request, 'main_app/wedding_detail.html', {'wedding': wedding, 'event_form': event_form})

def add_event(request, wedding_id):
    form = EventForm(request.POST)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.wedding_id = wedding_id
        new_event.save()
    return redirect('weddings_detail', wedding_id=wedding_id)

class WeddingList(ListView):
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

class EventDetail(DetailView):
    model = Event

class EventDelete(DeleteView):
    model = Event
    def get_success_url(self):
        wedding = self.object.wedding 
        return reverse('weddings_detail', kwargs={'wedding_id': wedding.id})
    
class EventUpdate(UpdateView):
    model = Event
    fields = ['description', 'start_date_time', 'end_date_time', 'venue']
    
