from django.shortcuts import render
from django.http import HttpResponse
from apl.models import *

def vista1(request):
    
    
    return render(request, 'index.html')

def vista2(request):
    
    
    return render(request, 'index2.html')