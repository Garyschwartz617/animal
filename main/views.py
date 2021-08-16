from django.shortcuts import render
from .models import Family,Animal
# Create your views here.

def homepage(request):
    return render(request,'index.html')

def family(request, num):
    context = {'family': Family.objects.get(id = num)}
    return render(request,'family.html', context)

def animal(request, num):
    context = {'animal': Animal.objects.get(id = num)}
    return render(request,'animal.html', context)

def animal1(request):
    context =  {'animal': Animal.objects.all()}
    return render(request,'animal1.html', context)