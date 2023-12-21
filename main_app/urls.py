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
    path('weddings/<int:wedding_id>/add_guest/', views.add_guest, name='add_guest'),

    path('events/<int:pk>/', views.EventDetail.as_view(), name='events_detail'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:event_id>/assoc_guest/<int:guest_id>', views.assoc_guest, name='assoc_guest'),
    path('events/<int:event_id>/unassoc_guest/<int:guest_id>', views.unassoc_guest, name='unassoc_guest'),
    
    path('accounts/signup', views.signup, name='signup'),
]
