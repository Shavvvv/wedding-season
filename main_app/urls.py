from django.urls import path
from . import views


# Defined url routes
urlpatterns = [
    path('', views.home, name='home'),
    path('weddings/', views.WeddingList.as_view(), name='weddings_list'),
    path('weddings/<int:wedding_id>/', views.weddings_detail, name='weddings_detail'),
    path('weddings/create/', views.WeddingCreate.as_view(), name='weddings_create'),
    path('weddings/<int:pk>/delete/', views.WeddingDelete.as_view(), name='weddings_delete'),
    path('weddings/<int:pk>/update/', views.WeddingUpdate.as_view(), name='weddings_update'),
    path('weddings/<int:wedding_id>/add_event/', views.add_event, name='add_event'),

    path('events/<int:pk>/', views.EventDetail.as_view(), name='events_detail'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
]
