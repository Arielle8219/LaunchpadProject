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

    if request.method == 'POST':
      # create an instance of our form, and fill it with the POST data
      # when the user inputs data into the form

      form = InputForm(request.POST)

      # if the user inputs valid parameters, take them in and initialize variables 
      # for generating a graph
      if form.is_valid():
        startYear = form.cleaned_data['startYear']
        endYear = form.cleaned_data['endYear']
        countriesRaw = form.cleaned_data['countries']
        countriesList = []

        # TODO: make getting user input for multiple countries more elegant
        # and allow for greater variation in user input


        # breaks up a large raw string of countries into smaller, individual ones
        # divides them very primitively for now - slicing by commas
        # then applies fuzzy search on individual countries

        # side note - for forms, could probably create a new model for countries
        # using ISO data - something to think about
        while (countriesRaw.find(',') != -1):
            countrySubstr = countriesRaw[0 : countriesRaw.find(',')]
            countriesRaw = countriesRaw[countriesRaw.find(',') + 2 :] 
            countryTemp = pycountry.countries.search_fuzzy(countrySubstr)[0].alpha_3
            countriesList.append(countryTemp)
        countryTemp = pycountry.countries.search_fuzzy(countriesRaw)[0].alpha_3
        countriesList.append(countryTemp)
        graphic = TreeLossChart(startYear, endYear, countriesList)

    else:
        # GET request, so create an empty form with base values for the graphic
        form = InputForm()
        graphic = TreeLossChart(2000, 2020, [])
    
    # very simple html template with rendered graphic and input form
    return render(request, 'homepage.html', {'graphic':graphic, 'form': form})
def about(request):
    return HttpResponse("hello")