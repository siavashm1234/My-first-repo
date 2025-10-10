from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('use new in the url')
def index_new (request):
    return HttpResponse('new shirts')