#################################
# Exploratory Data Analysis Lab #
#################################

import pandas as pd
import numpy as np

path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
print(df.head())

# Save a local copy of original file in case website gets removed later on
# df.to_csv('original_df.csv')

import matplotlib.pyplot as plt
import seaborn as sns

# list the data types for each column
print(df.dtypes)

#########################################################
# Question 1                                            #
# What is the data type of the column "peak-rpm"?       #
#########################################################

print("\nQUESTION 1\n")
print(df['peak-rpm'].dtype)

#%%

# For example, we can calculate the correlation between variables of type "int64" or "float64"
# using the method "corr":

print(df.corr())

#########################################################################################################
# Question 2                                                                                            #
# Find the correlation between the following columns: bore, stroke,compression-ratio , and horsepower.  #
#                                                                                                       #
# Hint: if you would like to select those columns use the following syntax:                             #
# df[['bore','stroke' ,'compression-ratio','horsepower']]                                               #
#########################################################################################################

print("\nQUESTION 2\n")
df_corr = df[['bore','stroke' ,'compression-ratio','horsepower']].corr()
print(df_corr)

#%%

# Positive Linear Relationship

# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
# plt.show()    <- Uncomment to show graph
plt.close()

# The plot suggests a positive correlation between engine size and price.
# Calculate the correlation between engine size and price
df[["engine-size", "price"]].corr()

# Negative Linear Relationship

# Highway mpg is a potential predictor variable of price
sns.regplot(x="highway-mpg", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()

# We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately -0.704
print('\n')
print(df[['highway-mpg', 'price']].corr())

# Weak Linear Relationship
# Let's see if "Peak-rpm" as a predictor variable of "price".
sns.regplot(x="peak-rpm", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()

# We can examine the correlation between 'peak-rpm' and 'price' and see it's approximately -0.101616
print('\n')
print(df[['peak-rpm','price']].corr())

#################################################################################
# Question 3a                                                                   #
# Find the correlation between x="stroke", y="price".                           #
#                                                                               #
# Hint: if you would like to select those columns use the following syntax:     #
# df[["stroke","price"]]                                                        #
#################################################################################

print("\nQUESTION 3a\n")

# Calculate the correlation between stroke and price (=0.08231)
print(df[['stroke','price']].corr())

#####################################################################################################
# Question 3b                                                                                       #
# Given the correlation results between "price" and "stroke" do you expect a linear relationship?   #
#                                                                                                   #
# Verify your results using the function "regplot()".                                               #
#####################################################################################################

# Answer: No, the Pearson correlation is close to 0 which means a weak relationship.

# Plot regression plot for visual aid
sns.regplot(x="stroke", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()