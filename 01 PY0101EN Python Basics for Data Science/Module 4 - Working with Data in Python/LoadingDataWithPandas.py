#################################################
# Loading Data with Pandas Quick Practice Lab
#################################################

print("Loading Data with Pandas Quick Practice Lab")

# You will use the dataframe df for the following:

import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})

# 1) Plot the first three rows:

print("1) Plot the first three rows:")

print(df.head(3))

# 2) Obtain column  'a'

print("2) Obtain column  'a'")

print(df['a'])