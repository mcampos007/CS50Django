from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, wordl!")

def mario(request):
    return HttpResponse("Hello, Marito!!")

def karina(request):
    return HttpResponse("Hello, Karina!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")