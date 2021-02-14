import bs4
import requests
import pandas as pd
import numpy as np
import boto3

def get_basketball_stats(link='https://en.wikipedia.org/wiki/Michael_Jordan'):
    # read the webpage 
    response = requests.get(link)
    # create a BeautifulSoup object to parse the HTML  
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # the player stats are defined  with the attribute CSS class set to 'wikitable sortable'; 
    # therefore we create a tag object "table"
    table=soup.find(class_='wikitable sortable')

    # the headers of the table are the first table row (tr) we create a tag object that has the first row  
    headers=table.tr
    # the table column names are displayed  as an abbreviation; therefore we find all the abbr tags and returs an Iterator
    titles=headers.find_all("abbr")
    # we create a dictionary  and pass the table headers as the keys 
    data = {title['title']:[] for title in titles}
   # we will store each column as a list in a dictionary, the header of the column will be the dictionary key 

    # we iterate over each table row by finding each table tag tr and assign it to the object
    for row in table.find_all('tr')[1:]:
    
        # we iterate over each cell in the table, as each cell corresponds to a different column we all obtain the corresponding key corresponding the column n 
        for key,a in zip(data.keys(),row.find_all("td")[2:]):
            # we append each elment and strip any extra HTML content 
            data[key].append(''.join(c for c in a.text if (c.isdigit() or c == ".")))

    # we remove extra rows by finding the smallest list     
    Min=min([len(x)  for x in data.values()])
    # we convert the elements in the key to floats 
    for key in data.keys():
    
        data[key]=list(map(lambda x: float(x), data[key][:Min]))
       
    return data


#############################################################
# Question 1                                                #
# Web Scraping the data and Converting to Pandas Dataframe  #
#############################################################

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

links=['https://en.wikipedia.org/wiki/Michael_Jordan'\
       ,'https://en.wikipedia.org/wiki/Kobe_Bryant'\
      ,'https://en.wikipedia.org/wiki/LeBron_James'\
      ,'https://en.wikipedia.org/wiki/Stephen_Curry']

names=['Michael Jordan','Kobe Bryant','Lebron James','Stephen Curry']

# You can use the function get_basketball_stats to extract the Regular season table
# and store it to a Python dictionary.
# For example, you can extract the table for Michael Jordan and convert it to a Python dictionary
# as follows:

#using the link

# michael_jordan_dict=get_basketball_stats('https://en.wikipedia.org/wiki/Michael_Jordan')

#using the list

# michael_jordan_dict=get_basketball_stats(links[0])

#####################################################################################
# Question 1a                                                                       #
# For each Player create a Python dictionary from the table Regular season table    #
#####################################################################################

player_dicts = [get_basketball_stats(link) for link in links]

#########################################################################
# Question 1b                                                           #
# For each Player convert the Python Dictionary to a Pandas Dataframe   #
# using the constructor pd.DataFrame()                                  #
#########################################################################

player_df = [pd.DataFrame(dict) for dict in player_dicts]

##############################################################################################
# Question 1c                                                                                #
# For each player display the first five rows of the Dataframe,                              #
# print the name of each Player above the Dataframe.                                         #
# If you perform the process in a loop you will have to use the function display as follows: #
# display(df)                                                                                #
##############################################################################################

for i, player in enumerate(player_df):
    print(names[i] + " Stats\n")
    print(player.iloc[0:5])

#########################################################################
# Question 2                                                            #
# Plot the Points per game for a player using the function plt.plot()   #
#########################################################################

# Import the plotting library

import matplotlib.pyplot as plt

