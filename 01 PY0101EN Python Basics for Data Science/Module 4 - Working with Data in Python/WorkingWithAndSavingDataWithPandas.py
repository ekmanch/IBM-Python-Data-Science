###############################################################
# Working with and Saving Data with Pandas Quick Practice Lab
###############################################################

# You will use the dataframe df for the following:

import pandas as pd

df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})

# 1) Find the unique values in column  'a' :

print("1) Find the unique values in column  'a' :")

print(df['a'].unique())

# 2) Return a dataframe with only the rows where column  a  is less than two

print("2) Return a dataframe with only the rows where column  a  is less than two")

print(df[df['a']<2])