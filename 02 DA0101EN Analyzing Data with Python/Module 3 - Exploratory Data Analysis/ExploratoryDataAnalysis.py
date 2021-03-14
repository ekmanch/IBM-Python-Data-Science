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

#%%

# Categorical variables boxplot
sns.boxplot(x="body-style", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()

# Trying a different variable that might be better predictor of price
sns.boxplot(x="engine-location", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()

# Trying another variable that will turn out to be a good predictor of price
sns.boxplot(x="drive-wheels", y="price", data=df)
# plt.show()    <- Uncomment to show graph
plt.close()

# Let's take a look at the variables by utilizing a description method.
print('\n', df.describe())

# The default setting of "describe" skips variables of type Object.
# We can apply the method "describe" on the variables of type 'object' as follows:
print('\n', df.describe(include=['object']))

# Value counts only works on Pandas series, not dataframes, so only one set of [] brackets
print('\n', df['drive-wheels'].value_counts())

# We can convert the series to a Dataframe as follows:
df['drive-wheels'].value_counts().to_frame()

# Convert series to dataframe and rename column drive-wheels
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# Rename index of drive-wheels
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

# We can repeat the above process for the variable 'engine-location'.
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)

# let's group by the variable "drive-wheels".
# We see that there are 3 different categories of drive wheels.
print(df['drive-wheels'].unique())

# We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one".
df_group_one = df[['drive-wheels','body-style','price']]

# We can then calculate the average price for each of the different categories of data.
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
print('\n', df_group_one)

# You can also group with multiple variables.
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print('\n', grouped_test1)

# This grouped data is much easier to visualize when it is made into a pivot table.
# In this case, we will leave the drive-wheel variable as the rows of the table,
# and pivot body-style to become the columns of the table:
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print('\n', grouped_pivot)

# We don't have values for all categories. Replace NaN by zero (0)
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
print('\n', grouped_pivot)

#%%

#################################################################################################
# Question 4                                                                                    #
# Use the "groupby" function to find the average "price" of each car based on "body-style" ?    #
#################################################################################################

df_group_one = df[['drive-wheels','body-style','price']]
df_body_style = df_group_one.groupby(['body-style'],as_index=False).mean()
print('\n', df_body_style)

#%%

# Let's use a heat map to visualize the relationship between Body Style vs Price.
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
# plt.show()    <- Uncomment to show graph
plt.close()

# The default labels convey no useful information to us. Let's change that:
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
# plt.show()    <- Uncomment to show graph
plt.close()

# Pearson Correlation is the default method of the function "corr".
# Like before we can calculate the Pearson Correlation of the of the 'int64' or 'float64' variables.
df.corr()

# We can obtain P-value for the correlation (value between 0 and +1)
# Probability that the correlation is statistically significant
# using "stats" module in the "scipy" library.
from scipy import stats

# Let's calculate the Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Let's calculate the Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Let's calculate the Pearson Correlation Coefficient and P-value of 'length' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Let's calculate the Pearson Correlation Coefficient and P-value of 'width' and 'price':
pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )

# Let's calculate the Pearson Correlation Coefficient and P-value of 'curb-weight' and 'price':
pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Let's calculate the Pearson Correlation Coefficient and P-value of 'engine-size' and 'price':
pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# Let's calculate the Pearson Correlation Coefficient and P-value of 'bore' and 'price':
pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value )

# We can relate the process for each 'City-mpg' and 'Highway-mpg':
# City-mpg vs Price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

# Highway-mpg vs Price
pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value )

#%%

# ANOVA - Analysis of Variance
# Let's see if different types 'drive-wheels' impact 'price', we group the data.
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
print('\n', grouped_test2.head(2))
print('\n', df_gptest)

# We can obtain the values of the method group using the method "get_group".
print('\n', grouped_test2.get_group('4wd')['price'])

# we can use the function 'f_oneway' in the module 'stats' to obtain the F-test score and P-value.
# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val)

# This is a great result, with a large F test score showing a strong correlation
# and a P value of almost 0 implying almost certain statistical significance.
# But does this mean all three tested groups are all this highly correlated?

# Separately: fwd and rwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val )

# 4wd and rwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])  
   
print( "ANOVA results: F=", f_val, ", P =", p_val)

# 4wd and fwd
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])  
 
print("ANOVA results: F=", f_val, ", P =", p_val)

