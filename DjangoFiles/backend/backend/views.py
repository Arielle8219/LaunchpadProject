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
    #FIXME: it's not finding the csv file
    #df = pd.read_csv('treecover_loss_by_region__ha.csv')
    # TODO: pass in image data to an html template
    # take in user input? 
    # also figure out how to convert image data into an actual image
    # possibly relevant stack overflow: https://stackoverflow.com/questions/47263773/add-image-data-to-html-file
    countries = ["USA"]
    graphic = TreeLossChart(2004, 2020, countries)
    #return HttpResponse('<h1>Hello Django!</h1>')
    return render(request, 'homepage.html', {'graphic':graphic})

def about(request):
    return HttpResponse('about page')