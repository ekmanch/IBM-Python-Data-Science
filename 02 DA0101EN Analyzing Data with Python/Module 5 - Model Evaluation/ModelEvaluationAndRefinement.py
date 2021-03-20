#########################################
# Model Evaluation and Refinement Lab   #
#########################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import PolynomialFeatures
from ipywidgets import interact, interactive, fixed, interact_manual
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Import clean data 
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df = pd.read_csv(path)
# df.to_csv('module_5_auto.csv')    <- Uncomment to save CSV

# Functions for plotting

def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color="r", label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')
    plt.legend()

    plt.show()
    plt.close()

def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    
    
    #training data 
    #testing data 
    # lr:  linear regression object 
    #poly_transform:  polynomial transformation object 
 
    xmax=max([xtrain.values.max(), xtest.values.max()])

    xmin=min([xtrain.values.min(), xtest.values.min()])

    x=np.arange(xmin, xmax, 0.1)


    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()

def f(order, test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_data, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_pr,y_train)
    PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train,y_test, poly, pr)

#%%

# Part 1: Training and Testing

y_data = df['price']
x_data=df.drop('price',axis=1)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)


print("number of test samples :", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

#####################################################################################################
# Question 1                                                                                        #
# Use the function "train_test_split" to split up the data set such that 40% of the data samples    #
# will be utilized for testing, set the parameter "random_state" equal to zero.                     #
# The output of the function should be the following:                                               #
# "x_train_1" , "x_test_1", "y_train_1" and "y_test_1".                                             #
#####################################################################################################

print("\nQuestion 1\n")

x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)

print("number of test samples :", x_test_1.shape[0])
print("number of training samples:",x_train_1.shape[0])

#########################################################################
# Question 2                                                            #
# Find the R^2 on the test data using 40% of the data for training data #
#########################################################################

print("\nQuestion 2\n")

# Linear Regression object
lre = LinearRegression()

# Do a Linear Regression fit of the training data with 40/60 test/train split
lre.fit(x_train_1[['horsepower']], y_train_1)

print("R^2 score on test data: ", lre.score(x_test_1[['horsepower']], y_test_1))

print("R^2 score on training data: ", lre.score(x_train_1[['horsepower']], y_train_1))

#####################################################################################
# Question 3                                                                        #
# Calculate the average R^2 using two folds,                                        #
# find the average R^2 for the second fold utilizing the horsepower as a feature    #
#####################################################################################

print("\nQuestion 3\n")

Rcross_1 = cross_val_score(lre, x_data[['horsepower']], y_data, cv=2)

print("Avg R^2 score on each fold:", Rcross_1)

print("The mean of the folds are", Rcross_1.mean(), "and the standard deviation is" , Rcross_1.std())

#%%

# Part 2: Overfitting, Underfitting and Model Selection

# Below can only be used in jupyter notebooks
# interact(f, order=(0, 6, 1), test_data=(0.05, 0.95, 0.05))

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.45, random_state=0)

#########################################################################
# Question 4a                                                           #
# We can perform polynomial transformations with more than one feature. #
# Create a "PolynomialFeatures" object "pr1" of degree two?             #
#########################################################################

print("\nQuestion 4\n")

pr1 = PolynomialFeatures(degree=2)

#################################################################
# Question 4b                                                   #
# Transform the training and testing samples for the features   #
# 'horsepower', 'curb-weight', 'engine-size' and 'highway-mpg'. #
# Hint: use the method "fit_transform" ?                        #
#################################################################

x_train_pr1 = pr1.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
x_test_pr1 = pr1.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])

#####################################################################################
# Question 4c                                                                       #
# How many dimensions does the new feature have? Hint: use the attribute "shape"    #
#####################################################################################

print("The train set has", x_train_pr1.shape, "dimensions")
print("The test set has", x_test_pr1.shape, "dimensions")

#####################################################################
# Question 4d                                                       #
# Create a linear regression model "poly1" and train                #
# the object using the method "fit"using the polynomial features?   #
#####################################################################

poly1 = LinearRegression()
poly1.fit(x_train_pr1, y_train)

#############################################################################
# Question 4e                                                               #
# Use the method "predict" to predict an output on the polynomial features, #
# then use the function "DistributionPlot" to display the distribution of   #
# the predicted output vs the test data?                                    #
#############################################################################

yhat_poly1 = poly1.predict(x_test_pr1)

Title = 'Distribution  Plot of  Predicted Value Using Test Data vs Test Data Distribution'
# Uncomment below if you want to plot the graph
# DistributionPlot(y_test, yhat_poly1, "Actual Values (Test)", "Predicted Values (Test)", Title)

#############################################################################
# Question 4f                                                               #
# Using the distribution plot above, explain in words about the two regions #
# where the predicted prices are less accurate than the actual prices       #
#############################################################################

# The predicted values is higher than the actual values around 10k.
# The predicted values are also lower than the actual values around 30-40k?
# The model is not entirely accurate in these two regions.

#%%

# Part 3: Ridge regression

pr=PolynomialFeatures(degree=2)
x_train_pr=pr.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr=pr.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

#################################################################################
# Question 5                                                                    #
# Perform Ridge regression and calculate the R^2 using the polynomial features, #
# use the training data to train the model and test data to test the model.     #
# The parameter alpha should be set to 10.                                      #
#################################################################################

print("\nQuestion 5\n")

RigeModel=Ridge(alpha=10)

RigeModel.fit(x_train_pr, y_train)

print("The R^2 score of the ridge regression model with alpha = 10 is", RigeModel.score(x_test_pr, y_test))

#%%

# Part 4: Grid Search

#####################################################################################
# Question 6                                                                        #
# Perform a grid search for the alpha parameter and the normalization parameter,    #
# then find the best values of the parameters                                       #
#####################################################################################

print("\nQuestion 6\n")

parameters2= [{
    'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000],
    'normalize': [True, False]
    }]

Grid2 = GridSearchCV(Ridge(), parameters2,cv=4)

Grid2.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data)

BestRR2 = Grid2.best_estimator_
print("The best estimator after Grid Search is:", BestRR2)

BestRR2_score = BestRR2.score(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test)

print("The R^2 score of the best estimator is:", BestRR2_score)