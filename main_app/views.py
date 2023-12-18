from django.shortcuts import render
from django.views.generic import DetailView

from .models import Wedding

# Create your views here.
def home(request):
    return render(request, 'home.html')

class WeddingDetail(DetailView):
    model = Wedding