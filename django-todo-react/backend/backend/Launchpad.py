import pandas as pd
import pycountry
from matplotlib import pyplot as plt
import numpy as np
from io import StringIO

#TODO: find more data to use: for example, carbon dioxide emissions/tree cover gain

df = pd.read_csv('Tree cover loss in United States compared to other areas/treecover_loss_by_region__ha.csv')

# FIXME: fuzzy search doesn't quite work as intended - eg: England returns nothing
print("Enter number of countries: ")
countryCount = int(input())

inputCountry = []

print("Input start year: ")
startYear = int(input())

print("Input end year: ") 
endYear = int(input())
# loop for multiple inputs of countries from user
for i in range(countryCount):
    print("Input country: ")
    countryTemp = input()

    # Using pycountry to convert user input for country names into iso equivalents
    countryTemp = pycountry.countries.search_fuzzy(countryTemp)[0].alpha_3
    inputCountry.append(countryTemp)

fig_size = (10, 5)
f = plt.figure(figsize=fig_size)


def TreeLossChart(df, startYear, endYear, inputCountry):
    #TODO: delete this block of code later, kept in case needed for referencing
    """ newdf = df.loc(axis = 0)[(df['iso'] == inputCountry[0]) & (df['Year'] >= startYear) & (df['Year'] <= endYear)]
    print(newdf)
    newdf = newdf.set_index(['Year'])
    newdf = newdf.drop(['gfw_gross_emissions_co2e_all_gases__Mg'], axis=1)
    # ax refers to the plot
    ax = newdf.plot()
    del inputCountry[0] """

    lines = []
    labels = []
    ax = f.add_subplot(1,1,1)
    fig = plt.figure()

    for i in inputCountry: 
        # iterates through the list of user-inputted countries, filters through the dataframe
        # and creates a new dataframe based on user input for start/end year and country
        newdf2 = df.loc(axis = 0)[(df['iso'] == i) & (df['Year'] >= startYear) & (df['Year'] <= endYear)]
        """
        Remove this block later, kept in case needed
        newdf2 = newdf2.set_index(['Year'])
        newdf2 = newdf2.drop(['gfw_gross_emissions_co2e_all_gases__Mg'], axis=1)
        """
        # plots each individual column on the same graph, with the label as the country name
        plt.plot(newdf2['Year'], newdf2['umd_tree_cover_loss__ha'], label = pycountry.countries.get(alpha_3=i).name)
    


    plt.legend(loc = "best")
    plt.xlabel("Years")
    plt.ylabel("Tree Cover Loss (Hectares)")
    plt.show()
    
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

TreeLossChart(df, startYear, endYear, inputCountry)


