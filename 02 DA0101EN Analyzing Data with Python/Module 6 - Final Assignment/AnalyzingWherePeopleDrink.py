#################################
# Final Assignment              #
# Analyzing Where People Drink  #
#################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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

print(df.groupby('continent').sum())