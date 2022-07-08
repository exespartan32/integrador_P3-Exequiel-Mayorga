from django.shortcuts import render
from .models import Diario

# Create your views here.
def diario(request):
    data = Diario.objects.all()
    return render(request, 'app_integrador/home.html', {'noticias': data})