from django.urls import path
from . import views

urlpatterns = [
    path('', views.ITAssistant, name='home'),
    path('Devices/', views.devices, name='devices'),
]
