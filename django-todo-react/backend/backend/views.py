from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from . import Launchpad
import pandas as pd
# Create your views here.
def home(request):
    
    df = pd.read_csv('Tree cover loss in United States compared to other areas/treecover_loss_by_region__ha.csv')
    # TODO: pass in image data to an html template
    # take in user input? 
    # also figure out how to convert image data into an actual image
    # possibly relevant stack overflow: https://stackoverflow.com/questions/47263773/add-image-data-to-html-file
    context['graph'] = Launchpad.TreeLossChart(df, 2004, 2020, ["USA"])
    return HttpResponse('<h1>Hello Django!</h1>')
    # return render(request, 'x/dashboard.html', context)

def about(request):
    return HttpResponse('about page')