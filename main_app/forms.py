from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Event, User, Profile


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['type', 'description', 'start_date_time', 'end_date_time', 'venue']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['type']