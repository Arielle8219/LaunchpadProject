import pandas as pd
import pycountry
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('Tree cover loss in United States compared to other areas/treecover_loss_by_region__ha.csv')

# print(df['umd_tree_cover_loss__ha'].describe())
# FIXME: fuzzy search doesn't quite work as intended - eg: England returns nothing
print("Enter number of countries: ")
countryCount = int(input())


print("Input country: ")
inputCountry = []
i = 0
while(i < countryCount):
    countryTemp = input()
    # convert user input country names into ISO 
    inputCountry.extend(pycountry.countries.search_fuzzy(countryTemp)[0].alpha_3)
    i+=1


print("Input start year: ")
startYear = int(input())

print("Input end year: ") 
endYear = int(input())

#for (i in range(len(inputCountry))): 
df = df.loc(axis = 0)[(df['iso'] == inputCountry[0]) & (df['Year'] >= startYear) & (df['Year'] <= endYear)]

df = df.set_index(['Year'])

df = df.drop(['gfw_gross_emissions_co2e_all_gases__Mg'], axis=1)

# FIXME: throwing weird error fix later - matplotlib deprecation error

# plt.xticks(np.arange(startYear, endYear, 1))
df.plot()


plt.xlabel("Years")
plt.ylabel("Tree Cover Loss (Hectares)")
plt.show()


