from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Este es un mensaje desde el index")

def January(request):
    return HttpResponse("Walk for least 30 min every day")

def February(request):
    return HttpResponse("Go to the gym every day")

def March(request):
    return HttpResponse("Read at least 3 pages every day")

def April(request):
    return HttpResponse("Eat vegetables every day")

def May(request):
    return HttpResponse("Take my medications every night")

def June(request):
    return HttpResponse("Drink 2 liters of water every day")

def July(request):
    return HttpResponse("Do not drink too much coffee")

def August(request):
    return HttpResponse("See a psychologist at least 1 day a week")

def September(request):
    return HttpResponse("I seleep every day at the same time")

def October(request):
    return HttpResponse("Do meditacion every evening")

def November(request):
    return HttpResponse("Writing in a journal")

def December(request):
    return HttpResponse("Learning to save")
