from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getserverid(request):
    return HttpResponse("1")