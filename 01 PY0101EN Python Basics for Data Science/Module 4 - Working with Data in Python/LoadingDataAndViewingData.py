#################################################
# Loading Data and Viewing Data Lab
#################################################

print("Quiz on DataFrame")

import pandas as pd

# Saving Dataframe from Excel (XSLX)

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)

# Saving Dataframe from CSV

#csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
#df = pd.read_csv(csv_path)


# Question 1

# Use a variable q to store the column Rating as a dataframe

print("Question 1: Use a variable q to store the column Rating as a dataframe")

q = df[['Rating']]

print(q)

# Assign the variable q to the dataframe that is made up of the column Released and Artist:

print("Question 2: Assign the variable q to the dataframe that is made up of the column Released and Artist:")

q = df[['Released', 'Artist']]

print(q)

# Access the 2nd row and the 3rd column of df:

print("Question 3: Access the 2nd row and the 3rd column of df:")

print(df.iloc[1,2])

# Use the following list to convert the dataframe index df to characters and assign it to df_new;
# find the element corresponding to the row index a and column 'Artist'.
# Then select the rows a through d for the column 'Artist'
# new_index=['a','b','c','d','e','f','g','h']

print("Question 4:")
print("Convert the dataframe index df to characters and assign it to df_new\n\n")

new_index=['a','b','c','d','e','f','g','h']

df_new = df.set_axis(new_index)

print("Answer:\n", df_new, "\n")

print("Find the element corresponding to the row index 'a' and column 'Artist'\n\n")

print("Answer: ", df_new.loc['a', 'Artist'], "\n")

print("Select rows 'a' through 'd' for the column 'Artist'\n\n")

print("Answer:\n", df_new.loc['a':'d','Artist'])