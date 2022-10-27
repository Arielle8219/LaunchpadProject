import pandas as pd
import pycountry
from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO
import base64


#TODO: find more data to use: for example, carbon dioxide emissions/tree cover gain
"""
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


"""

def TreeLossChart(startYear, endYear, inputCountry):    
    df = pd.read_csv('treecover_loss_by_region__ha.csv')
    
    #instantiates the figure
    fig_size = (10, 5)
    f = plt.figure(figsize=fig_size)
    lines = []
    labels = []
    ax = f.add_subplot(1,1,1)
    fig = plt.figure()

    # iterates through the list of user-inputted countries, filters through the dataframe
    # and creates a new dataframe based on user input for start/end year and country
    for i in inputCountry: 
        newdf2 = df.loc(axis = 0)[(df['iso'] == i) & (df['Year'] >= startYear) & (df['Year'] <= endYear)]
        
        # plots each individual column on the same graph, with the label as the country name
        plt.plot(newdf2['Year'], newdf2['umd_tree_cover_loss__ha'], label = pycountry.countries.get(alpha_3=i).name)
    

    # setting legend and axes
    plt.legend(loc = "best")
    plt.xlabel("Years")
    plt.ylabel("Tree Cover Loss (Hectares)")
    #plt.show()
    plt.tight_layout()

    # preparing graph to be imported as an image and uploaded onto an html file
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic


#TreeLossChart(startYear, endYear, inputCountry)


