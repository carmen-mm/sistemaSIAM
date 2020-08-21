from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request,'practicasMedicas/index.html')
 # return HttpResponse("Hola mundo, probando las vistas")
