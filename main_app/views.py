from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Wedding, Event, Profile
from .forms import EventForm, GuestForm, UserForm, ProfileForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def weddings_detail(request, wedding_id):
    wedding = Wedding.objects.get(id=wedding_id)
    event_form = EventForm()
    guest_form = GuestForm()
    return render(request, 'main_app/wedding_detail.html', {'wedding': wedding, 'event_form': event_form, 'guest_form': guest_form})

@login_required
def add_event(request, wedding_id):
    form = EventForm(request.POST)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.wedding_id = wedding_id
        new_event.save()
    return redirect('weddings_detail', wedding_id=wedding_id)

@login_required
def add_guest(request, wedding_id):
    form = GuestForm(request.POST)
    if form.is_valid():
        new_guest = form.save(commit=False)
        new_guest.wedding_id = wedding_id
        new_guest.save()
    return redirect('weddings_detail', wedding_id=wedding_id)

class WeddingList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Wedding.objects.filter(profiles__id=self.request.user.profile.id)

class WeddingCreate(LoginRequiredMixin, CreateView):
    model = Wedding
    fields = ['name', 'description']

    def form_valid(self,form):
        #Many to Many id troubleshoot
        new_wedding=form.save()
        new_wedding.profiles.add(self.request.user.profile.id)
        new_wedding.save()
        return super().form_valid(form)

class WeddingDelete(LoginRequiredMixin, DeleteView):
    model = Wedding
    success_url = '/weddings/'

class WeddingUpdate(LoginRequiredMixin, UpdateView):
    model = Wedding
    fields = ['description']

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    def get_success_url(self):
        wedding = self.object.wedding 
        return reverse('weddings_detail', kwargs={'wedding_id': wedding.id})
    
class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['description', 'start_date_time', 'end_date_time', 'venue']
    
def signup(request):
    error_message =''
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user_id = user.id
            profile = profile_form.save()
            login(request, user)
            return redirect('weddings_list')
        else:
            error_message = 'Invalid sign up - try again'
    user_form = UserForm()
    profile_form = ProfileForm()
    context = {'user_form': user_form, 'profile_form': profile_form,'error_message': error_message}
    return render(request, 'registration/signup.html', context)