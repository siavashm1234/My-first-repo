from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home_template.html')


def room (request):
    return render(request , 'room.html')