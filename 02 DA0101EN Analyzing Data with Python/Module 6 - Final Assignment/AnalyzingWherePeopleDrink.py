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
print("Box Plot was shown")
sns.boxplot(x="continent", y="beer_servings", data=df)
# plt.show()    <- Uncomment to show box plot
plt.close()

#########################################################################
# Question 5                                                            #
# Use the function regplot in the seaborn library to determine if the   #
# number of wine servings is negatively or positively                   #
# correlated with the number of beer servings.                          #
#########################################################################

print("\nQuestion 5\n")

print("Scatter Plot was shown")

# From Scatter Plot below it seems like there is a positive correlation
sns.regplot(x="beer_servings", y="wine_servings", data=df)
plt.ylim(0,)
plt.show()
plt.close()

#################################################################################
# Question 6                                                                    #
# Fit a linear regression model to predict the 'total_litres_of_pure_alcohol'   #
# using the number of 'wine_servings' then calculate  𝑅2                        #
########################################################################################

