from django.urls import path
from . import views


# Defined url routes
urlpatterns = [
    path('', views.home, name='home'),
]
