from django.forms import ModelForm
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['type', 'description', 'start_date_time', 'end_date_time', 'venue']
