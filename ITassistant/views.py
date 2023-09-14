from django.shortcuts import render
from .models import Equipos
# Create your views here.

def index (request):
    equipos= Equipos.objects.all
    return render(
        request, 
        'index.html',
        context= {'equipos':equipos}
    )