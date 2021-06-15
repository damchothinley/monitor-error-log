from django.shortcuts import render
from django.http import HttpResponse  # newly added

# Create your views here.


def HomePageView(request):
    return HttpResponse("Hello World!")
