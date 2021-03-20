#################################
# Final Assignment              #
# Analyzing Where People Drink  #
#################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

df= pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/edx/project/drinks.csv')
# df.to_csv('original.csv')     <- Uncomment to save dataset

print("\nDataset Used in Final Assignment\n")
print(df.head())

#####################################################################
# Question 1                                                        #
# Display the data types of each column using the attribute dtype.  #
#####################################################################

print("\nQuestion 1\n")

print(df.dtypes)

#############################################################################
# Question 2                                                                #
# Use the method groupby to get the number of wine servings per continent   #
#############################################################################

print("\nQuestion 2\n")

df1 = df[['wine_servings', 'continent']]

print(df1.groupby('continent').sum())

#####################################################################################
# Question 3                                                                        #
# Perform a statistical summary and analysis of beer servings for each continent:   #
#####################################################################################

print("\nQuestion 3\n")

print(df['beer_servings'].describe())

#############################################################################
# Question 4                                                                #
# Use the function boxplot in the seaborn library to produce a plot         #
# that can be used to show the number of beer servings on each continent.   #
#############################################################################

print("\nQuestion 4\n")

