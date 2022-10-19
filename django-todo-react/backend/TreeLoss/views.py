from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# TODO: figure out how to link up python function with views
def TreeLossChart(request):
    return HttpResponse('<h1>Hello Django!</h1>')
