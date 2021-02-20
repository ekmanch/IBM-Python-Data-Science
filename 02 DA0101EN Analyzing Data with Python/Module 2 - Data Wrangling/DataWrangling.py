#################################
# Data Wrangling Lab            #
#################################


# You can find the "Automobile Data Set" from the following link:
# https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# URL for this dataset
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# Create a dataframe from the auto.csv dataset
df = pd.read_csv(filename, names = headers)

# Use the method head() to display the first five rows of the dataframe.
print(df.head())

#%%
# Multiple rows have ?s
# Convert "?" to NaN
df.replace("?", np.nan, inplace = True)
print(df.head(5))

#%%
# isnull() can be used to detect missing data
# The output is a boolean value indicating whether the value is in fact missing data.
# "True" stands for missing value, while "False" stands for not missing value.
missing_data = df.isnull()
print(missing_data.head(5))

#%% 
# Using a for loop in Python, we can quickly figure out the number of missing values in each column. 
# value_counts() can be used to count number of "True" and "False" boolean values
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

#%%
# Datasets with missing data can be fixed by:
# 1) Replace by the mean of the column
# 2) Replace by the max frequency of the column (i.e. most frequently occurring value)
# 3) Removing rows/columns with missing data

# Calculate the average of the column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

# Replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate the mean value for 'bore' column
avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

# Replace NaN by mean value
df["bore"].replace(np.nan, avg_bore, inplace=True)

#%%

#############################################################################
# Question 1                                                                #
# According to the example above, replace NaN in "stroke" column by mean.   #
#############################################################################

# Answer:
avg_stroke = df['stroke'].astype('float').mean(axis=0)
print("Average of stroke:", avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

#%%

# Calculate the mean value for the 'horsepower' column:
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

# Replace "NaN" by mean value:
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# Calculate the mean value for 'peak-rpm' column:
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)

# Replace NaN by mean value:
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

# To see which values are present in a particular column, we can use the ".value_counts()" method:
print(df['num-of-doors'].value_counts())

# We can see that four doors are the most common type.
# We can also use the ".idxmax()" method to calculate for us the most common type automatically:
print(df['num-of-doors'].value_counts().idxmax())

# The replacement procedure is very similar to what we have seen previously
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# Finally, let's drop all rows that do not have price data:
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

# print the first 5 rows to check result of the handling of the missing values
print(df.head())

#%%

#####################
# Data Formatting   #
#####################

# Lets list the data types for each column
print(df.dtypes)

# Convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Let us list the columns after the conversion
print(df.dtypes)

#%%

#########################
# Data Standardization  #
#########################

# The formula for converting miles per gallon (mpg) to L/100km is:
# L/100km = 235 / mpg
print(df.head())
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data 
print(df.head())

#%%

#############################################################################################
# Question 2                                                                                #
# According to the example above, transform mpg to L/100km in the column of "highway-mpg"   #
# and change the name of column to "highway-L/100km".                                       #
#############################################################################################

df['highway-mpg'] = 235/df["highway-mpg"]
df.rename(columns={'highway-mpg' : 'highway-L/100km'}, inplace=True)
print(df.head())

#%%

#########################
# Data Normalization    #
#########################

# To demonstrate normalization, let's say we want to scale the columns "length", "width" and "height"
# Target:would like to Normalize those variables so their value ranges from 0 to 1.
# Approach: replace original value by (original value)/(maximum value)

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

#%%

#####################################################################
# Question 3                                                        #
# According to the example above, normalize the column "height".    #
#####################################################################

df['height'] = df['height']/df['height'].max()
print(df[['length', 'width', 'height']].head())

#%%

#########################
# Binning Data          #
#########################

# Convert data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)

# Lets plot the histogram of horspower, to see what the distribution of horsepower looks like.
plt.hist(df["horsepower"])

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

# Show the graph of the histogram
# plt.show()    <- uncomment to see the graph

# Close figure
plt.close()

# We would like 3 bins of equal size bandwidth so we use
# numpy's linspace(start_value, end_value, numbers_generated) function.
# Since we want to include the minimum value of horsepower we want to set
# start_value=min(df["horsepower"]).
# Since we want to include the maximum value of horsepower we want to set
# end_value=max(df["horsepower"]).
# Since we are building 3 bins of equal length, there should be 4 dividers, so numbers_generated=4.
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)

# We set group names:
group_names = ['Low', 'Medium', 'High']

# We apply the function "cut" the determine what each value of "df['horsepower']" belongs to.
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
print(df[['horsepower','horsepower-binned']].head(20))

# Lets see the number of vehicles in each bin.
print(df["horsepower-binned"].value_counts())

# Lets plot the distribution of each bin.
plt.figure()
plt.bar(group_names, df['horsepower-binned'].value_counts())

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

# Show the bar graph
# plt.show()    <- uncomment to plot the bar graph

# Close bar graph
plt.close()

# Normally, a histogram is used to visualize the distribution of bins we created above.
# draw historgram of attribute "horsepower" with bins = 3
plt.figure()
plt.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
# plt.show()    <- uncomment to plot the histogram

# Close figure
plt.close()

#%%

#########################
# Indicator Variable    #
#########################

# We will use the panda's method 'get_dummies'
# to assign numerical values to different categories of fuel type.
print(df.columns)

# get indicator variables and assign it to data frame "dummy_variable_1"
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())

# change column names for clarity
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
print(dummy_variable_1.head())

# In the dataframe, column fuel-type has a value for 'gas' and 'diesel'as 0s and 1s now.
# concatenate data frame "df" with "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
print(df.head())

#%%

#####################################################################
# Question 4                                                        #
# As above, create indicator variable to the column of "aspiration" #
#####################################################################

aspiration_dummy = pd.get_dummies(df['aspiration'])
print(aspiration_dummy.head())

aspiration_dummy.rename(columns={'std' : 'aspiration-std', 'turbo' : 'aspiration-turbo'}, inplace=True)
print(aspiration_dummy.head())

df = pd.concat([df, aspiration_dummy], axis=1)
print(df.head())

df.drop("aspiration", axis = 1, inplace=True)
print(df.head())

# Save the new dataset to a new CSV file
df.to_csv('clean_df.csv')