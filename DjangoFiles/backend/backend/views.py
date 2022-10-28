# importing module
import sys
# appending a path
sys.path.append('/Users/arielledong/Desktop/LaunchpadProject')
from django.http import HttpResponse
from django.shortcuts import render
# im not sure if the module is importing correctly
from DjangoFiles.backend.backend.Launchpad import TreeLossChart
import pandas as pd
from backend.forms import InputForm
import pycountry
# Create your views here.
def home(request):
    
    # TODO: take in user input for countries, start year, and end year
    #countries = ['USA', 'DEU', 'GBR']
    if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      # when the user inputs data into the form
      form = InputForm(request.POST)
      if form.is_valid():
        startYear = form.cleaned_data['startYear']
        endYear = form.cleaned_data['endYear']
        countriesRaw = form.cleaned_data['countries']
        countriesList = []
        
        # user input is somewhat working, but because of the way
        # i've set up indexing, it never grabs the last value

        while (countriesRaw.find(',') != -1):
            countrySubstr = countriesRaw[0 : countriesRaw.find(',')]
            countriesRaw = countriesRaw[countriesRaw.find(',') + 1 :]
            countryTemp = pycountry.countries.search_fuzzy(countrySubstr)[0].alpha_3
            countriesList.append(countryTemp)
        
        graphic = TreeLossChart(startYear, endYear, countriesList)

    else:
        # this must be a GET request, so create an empty form
        form = InputForm()
        graphic = TreeLossChart(2000, 2020, [])
    
    
    
    # very simple html template with rendered graphic and input form
    return render(request, 'homepage.html', {'graphic':graphic, 'form': form})

def about(request):
    return HttpResponse('about page')