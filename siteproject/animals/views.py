from django.shortcuts import render
from .models import Animal

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})
