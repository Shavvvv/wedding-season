from django.urls import path
from . import views


# Defined url routes
urlpatterns = [
    path('', views.home, name='home'),
    path('weddings/<int:pk>/', views.WeddingDetail.as_view(), name='weddings_detail'),
]
