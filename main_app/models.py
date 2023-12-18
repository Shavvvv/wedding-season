from django.db import models
from django.urls import reverse
#from django.utils import timezone

EVENT_TYPES = (
    ('RD', 'Rehearsal Dinner'),
    ('RE', 'Reception'),
    ('WC', 'Wedding Ceremony')    
)

# Create your models here.
class Wedding(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weddings_detail', kwargs={'pk': self.pk})
    
class Event(models.Model):
    type = models.CharField(
        max_length=2,
        choices=EVENT_TYPES,
    )
    description = models.TextField(max_length=250)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    venue = models.CharField(max_length=100)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)

    def __str__(self):
        return f"Event: {self.get_type_display()}"
    
    def get_absolute_url(self):
        return reverse('events_list', kwargs={'pk': self.wedding.id})

    class Meta:
        ordering = ['start_date_time']
