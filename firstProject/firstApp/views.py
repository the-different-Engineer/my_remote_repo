from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
    s = "<h1> Prateek </h1>"
    return HttpResponse(s)
