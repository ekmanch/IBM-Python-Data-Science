#################################
# Model Development Lab         #
#################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
print(df.head())

# Uncomment to save the downloaded csv file
# df.to_csv('original_df.csv')

# load the modules for linear regression
from sklearn.linear_model import LinearRegression

#%%

# Linear Regression

#########################################
# Question 1a                           #
# Create a linear regression object?    #
#########################################

lm = LinearRegression()

#####################################################################
# Question 1b                                                       #
# Train the model using 'engine-size' as the independent variable   #
# and 'price' as the dependent variable?                            #
#####################################################################

X = df[['engine-size']]
Y = df['price']

yhat = lm.fit(X,Y)

#################################################
# Question 1c                                   #
# Find the slope and intercept of the model?    #
#################################################

print("Intercept of the linear regression model is: ", lm.intercept_)
print("Slope of the linear regression model is: ", lm.coef_)

#####################################################################################################
# Question 1d                                                                                       #
# What is the equation of the predicted line. You can use x and yhat or 'engine-size' or 'price'?   #
#####################################################################################################

yhat = lm.intercept_ + lm.coef_*df[['engine-size']]

#%%

# Multiple Linear Regression

#########################################################################
# Question 2a                                                           #
# Create and train a Multiple Linear Regression model "lm2"             #
# where the response variable is price,                                 #
# and the predictor variable is 'normalized-losses' and 'highway-mpg'.  #
#########################################################################

lm2 = LinearRegression()

Z = df[['normalized-losses', 'highway-mpg']]
Y = df['price']

lm2.fit(Z,Y)

#################################################
# Question 2b                                   #
# Find the coefficient of the model?            #
#################################################

print("The coefficients of the Multiple Linear Regression Model are: ", lm2.coef_)

#%%

# Model Evaluation Using Visualization

# import the visualization package: seaborn
import seaborn as sns

# Regression Plot

#########################################################################
# Question 3                                                            #
# Given the regression plots above,                                     #
# is "peak-rpm" or "highway-mpg" more strongly correlated with "price". #
# Use the method ".corr()" to verify your answer.                       #
#########################################################################

# You can see from this output that highway-mpg is much more strongly correlated with price
print(df[['peak-rpm', 'highway-mpg', 'price']].corr())

# Residual Plot

#%%

# Polynomial Regression and Pipelines

# Given Function:
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

#################################################################
# Question 4                                                    #
# Create 11 order polynomial model with the variables x and y.  #
#################################################################

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 11)
p = np.poly1d(f)
print(p)
PlotPolly(p, x, y, 'highway-mpg')

# Multivariate Polynomial Regression

from sklearn.preprocessing import PolynomialFeatures

#%%

# Pipelines

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#################################################################################################
# Question 5                                                                                    #
# Create a pipeline that Standardizes the data,                                                 #
# then perform prediction using a linear regression model using the features Z and targets y    #
#################################################################################################

Input=[('scale',StandardScaler()), ('model',LinearRegression())]

pipe = Pipeline(Input)

pipe.fit(Z,Y)

ypipe=pipe.predict(Z)

print("The predicted value from the Pipeline:\n", ypipe[0:10])

#%%

# Measures for In-Sample Evaluation

from sklearn.metrics import mean_squared_error

from sklearn.metrics import r2_score

#%%

# Prediction and Decision Making

import matplotlib.pyplot as plt
import numpy as np