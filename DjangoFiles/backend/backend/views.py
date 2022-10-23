# importing module
import sys
# appending a path
sys.path.append('/Users/arielledong/Desktop/LaunchpadProject')
from django.http import HttpResponse
from django.shortcuts import render
# im not sure if the module is importing correctly
from DjangoFiles.backend.backend.Launchpad import TreeLossChart
import pandas as pd

# Create your views here.
def home(request):
    
    # TODO: take in user input for countries, start year, and end year
    countries = ['USA']
    graphic = TreeLossChart(2004, 2020, countries)
    
    # very simple html template
    return render(request, 'homepage.html', {'graphic':graphic})

def about(request):
    return HttpResponse('about page')