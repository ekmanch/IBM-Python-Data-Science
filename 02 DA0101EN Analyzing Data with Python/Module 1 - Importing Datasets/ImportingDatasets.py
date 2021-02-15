#################################
# Importing Datasets Lab        #
#################################

# import pandas library
import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"
# Using https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)
df.to_csv('automobile_original.csv', index=False)

# show the first 5 rows using dataframe.head() method
print("\nThe first 5 rows of the dataframe:\n") 
print(df.head(5))

#################################################
# Question 1                                    #
# check the bottom 10 rows of data frame "df"   #
#################################################

print("\nThe last 10 rows of the dataframe:\n")
print(df.tail(10))

# To better describe our data we can introduce a header, this information is available at:
# https://archive.ics.uci.edu/ml/datasets/Automobile

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
#print("headers\n", headers)

df.columns = headers
print("\nThe first 10 rows with added header:\n")
print(df.head(10))

# we need to replace the "?" symbol with NaN so the dropna() can remove the missing values
df1=df.replace('?',np.NaN)

# we can drop missing values along the column "price" as follows
df=df1.dropna(subset=["price"], axis=0)
print("\nThe first 20 rows with all rows with NaN as price removed:\n")
print(df.head(20))

#################################################
# Question 2                                    #
# Find the name of the columns of the dataframe #
#################################################

print("\nThe columns of the dataset:\n")
print(df.columns)

# Save the dataset
df.to_csv("automobile.csv", index=False)

# Check the datatype of each column
print("\nCheck the datatypes of each column:\n")
print(df.dtypes)

# Check statistical data for each column, e.g. count, standard deviation, max/min, mean value
# This excludes NaN (i.e. object type = string type) columns
print("\nRead out various summary statistics for each column, excluding NaN:\n")
print(df.describe())

# describe all the columns, including those that are NaN (i.e. object type), in "df" 
print("\nRead out various statistical data for all columns, including NaN:\n")
print(df.describe(include = "all"))

#########################################################################################
# Question 3                                                                            #
# You can select the columns of a data frame by indicating the name of each column      #
# for example, you can select the three columns as follows:                             #
# dataframe[['column 1','column 2', 'column 3']]                                       #
# Where "column" is the name of the column, you can apply the method ".describe()"      #
# to get the statistics of those columns as follows:                                    #
# dataframe[['column 1','column 2', 'column 3'] ].describe()                           #
# Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.    #
#########################################################################################

print("\nCheck the statistical data for the columns 'length' and 'compression-ratio':\n")
print(df[['length', 'compression-ratio']].describe())

# Another method you can use to check your dataset is info()
# This method prints information about a DataFrame including
# the index dtype and columns, non-null values and memory usage.
print("\nPrint information on dataframe:\n")
print(df.info())

