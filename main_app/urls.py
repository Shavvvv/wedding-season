from django.urls import path
from . import views


# Defined url routes
urlpatterns = [
    path('', views.home, name='home'),
    path('weddings/', views.WeddingList.as_view(), name='weddings_list'),
    path('weddings/<int:pk>/', views.WeddingDetail.as_view(), name='weddings_detail'),
    path('weddings/create/', views.WeddingCreate.as_view(), name='weddings_create'),
    path('weddings/<int:pk>/delete', views.WeddingDelete.as_view(), name='weddings_delete'),
]
