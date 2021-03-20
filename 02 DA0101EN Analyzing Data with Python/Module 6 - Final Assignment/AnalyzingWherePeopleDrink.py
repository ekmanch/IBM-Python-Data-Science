#################################
# Final Assignment              #
# Analyzing Where People Drink  #
#################################

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

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
# plt.show()    <- Uncomment to show scatter plot
plt.close()

#################################################################################
# Question 6                                                                    #
# Fit a linear regression model to predict the 'total_litres_of_pure_alcohol'   #
# using the number of 'wine_servings' then calculate  𝑅2                        #
########################################################################################

print("\nQuestion 6\n")

lm = LinearRegression()

X = df[['wine_servings']]
Y = df[['total_litres_of_pure_alcohol']]

lm.fit(X,Y)

print("The R^2 score of the linear regression model is:", lm.score(X,Y))

#########################################################################################
# Question 7                                                                            #
# Use list of features to predict the 'total_litres_of_pure_alcohol',                   #
# split the data into training and testing and determine the  𝑅2  on the test data      #
#                                                                                       #
# Note: Please use test_size = 0.10 and random_state = 0 in the following questions.    #
#########################################################################################

print("\nQuestion 7\n")

lr = LinearRegression()

x_data = df.drop(['total_litres_of_pure_alcohol', 'continent', 'country'],axis=1)
y_data = df[['total_litres_of_pure_alcohol']]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.1, random_state=0)

lr.fit(x_train[['beer_servings', 'spirit_servings', 'wine_servings']], y_train)

print("The R^2 score of the model using test data is:", lr.score(x_test, y_test))

#########################################################################
# Question 8                                                            #
# Create a pipeline object that scales the data,                        #
# performs a polynomial transform and fits a linear regression model.   #
# Fit the object using the training data in the question above,         #
# then calculate the R^2 using the test data.                           #
# Take a screenshot of your code and the  𝑅2.                           #
# There are some hints in the notebook:                                 #
# 'scale'                                                               #
# 'polynomial'                                                          #
# 'model'                                                               #
#                                                                       #
# The second element in the tuple contains the model constructor:       #
# StandardScaler()                                                      #
# PolynomialFeatures(include_bias=False)                                #
# LinearRegression()                                                    #
#########################################################################

print("\nQuestion 8\n")

Input = [('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

pipe = Pipeline(Input)

pipe.fit(x_train,y_train)

print("The R^2 score of the model using test data is:", pipe.score(x_test, y_test))

#####################################################################
# Question 9                                                        #
# Create and fit a Ridge regression object using the training data, #
# setting the regularization parameter to 0.1 and calculate         #
# the  𝑅2  using the test data.                                     #
# Take a screenshot of your code and the  𝑅2                        #
#####################################################################

print("\nQuestion 9\n")

RidgeModel = Ridge(alpha=0.1)

RidgeModel.fit(x_train, y_train)

# The resulting R^2 is 0.699030454901918
print("The R^2 score of the model using test data is:", RidgeModel.score(x_test, y_test))

#########################################################################################
# Question 10                                                                           #
# Perform a 2nd order polynomial transform on both the training data and testing data.  #
# Create and fit a Ridge regression object using the training data,                     #
# setting the regularization parameter to 0.1.                                          #
# Calculate the  𝑅2  utilizing the test data provided.                                  #
# Take a screen-shot of your code and the  𝑅2.                                          #
#########################################################################################

print("\nQuestion 10\n")

pr = PolynomialFeatures(degree=2)

x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)

RidgeModel = Ridge(alpha=0.1)

RidgeModel.fit(x_train_pr, y_train)

# The resulting R^2 is 0.7076376228095793
print("The R^2 score of the model using test data is:", RidgeModel.score(x_test_pr, y_test))