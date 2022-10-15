import pandas as pd
import pycountry
from matplotlib import pyplot as plt
import numpy as np

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

for i in range(countryCount):
    print("Input country: ")
    countryTemp = input()
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
    for i in inputCountry: 

        newdf2 = df.loc(axis = 0)[(df['iso'] == i) & (df['Year'] >= startYear) & (df['Year'] <= endYear)]
        """
        Remove this block later, kept in case needed
        newdf2 = newdf2.set_index(['Year'])
        newdf2 = newdf2.drop(['gfw_gross_emissions_co2e_all_gases__Mg'], axis=1)
        """
        plt.plot(newdf2['Year'], newdf2['umd_tree_cover_loss__ha'], label = pycountry.countries.get(alpha_3=i).name)
        


    # FIXME: throwing weird error fix later - matplotlib deprecation error (also on line 53, but 
    # doesn't cause any errors atm)

    # plt.xticks(np.arange(startYear, endYear, 1))
    plt.legend(loc = "best")
    plt.xlabel("Years")
    plt.ylabel("Tree Cover Loss (Hectares)")
    plt.show()
    return(f)

TreeLossChart(df, startYear, endYear, inputCountry)


