from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#from django.utils import timezone

PROFILE_TYPES = (
    ('B', 'Bride'),
    ('G', 'Groom'),
    ('P', 'Planner')    
)

EVENT_TYPES = (
    ('RD', 'Rehearsal Dinner'),
    ('RE', 'Reception'),
    ('WC', 'Wedding Ceremony')    
)

RSVP_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(
        'Wedding Role',
        max_length=1,
        choices=PROFILE_TYPES,
    )
   
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Wedding(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    profiles = models.ManyToManyField(Profile)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weddings_detail', kwargs={'wedding_id': self.id})
    
class Event(models.Model):
    type = models.CharField(
        max_length=2,
        choices=EVENT_TYPES,
    )
    description = models.TextField(max_length=250)
    start_date_time = models.DateTimeField('Start Date and Time')
    end_date_time = models.DateTimeField('End Date and Time')
    venue = models.CharField(max_length=100)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)

    def __str__(self):
        return f"Event: {self.wedding.name} {self.get_type_display()}"
    
    def get_absolute_url(self):
        return reverse('events_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['start_date_time']

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    rsvp_choice = models.CharField(
        max_length=1,
        choices=RSVP_CHOICES,
        blank=True
    )
    dietary_restrictions = models.TextField(
        max_length=250,
        blank=True
    )
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)

    def __str__(self):
        return f"Guest: {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name', 'first_name']
