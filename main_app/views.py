from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import Wedding

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