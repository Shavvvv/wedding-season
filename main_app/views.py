from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Wedding

# Create your views here.
def home(request):
    return render(request, 'home.html')

class WeddingList(ListView):
    model = Wedding

class WeddingDetail(DetailView):
    model = Wedding