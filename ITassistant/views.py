from django.shortcuts import render
from .models import Devices
# Create your views here.

def ITAssistant (request):
    return render(
        request,
        'ITAssistant.html'
    )

def devices (request):
    devices= Devices.objects.all
    return render(
        request, 
        'devices.html',
        context= {'devices':devices}
    )