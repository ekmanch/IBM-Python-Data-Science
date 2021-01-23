######################################
# Dictionaries Lab 1
######################################

# You will need the dictionary D:

from typing import Dict


D={'a':0,'b':1,'c':2}

# Find the value for the key  'a'

print(D['a'])

# Find the keys of the dictionary D

print(D.keys())

######################################
# Dictionaries Quiz
######################################

# Question 1
# Consider the following dictionary:
D={'a':0,'b':1,'c':2}
# What is the result of the following: D.values()

# Answer prediction:
# answer will be a list of values in D, i.e. 0, 1 and 2

print(D.values())

# Question 2
# Consider the following dictionary:
D={'a':0,'b':1,'c':2}
# What is the output of the following D['b'] :

# Answer prediction:
# answer will be the value of key 'b', i.e. 1
print(D['b'])

######################################
# Dictionaries Lab 2
######################################

# Question 1
# You will need this dictionary for the next two questions:
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

# a) In the dictionary soundtrack_dic what are the keys ?

# Answer prediction
# "The Bodyguard" and "Saturday Night Fever"
print(soundtrack_dic.keys())

# b) In the dictionary soundtrack_dic what are the values ?

# Answer prediction
# "1992" and "1977"

print(soundtrack_dic.values())

# Question 2
# You will need this dictionary for the following questions:
# The Albums Back in Black, The Bodyguard and Thriller have the following
# music recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary album_sales_dict where the keys are
# the album name and the sales in millions are the values.

album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}

print(album_sales_dict)

# b) Use the dictionary to find the total sales of Thriller:

print(album_sales_dict["Thriller"])

# c) Find the names of the albums from the dictionary using the method keys():

print(album_sales_dict.keys())

# d) Find the values of the recording sales from the dictionary
# using the method values:

print(album_sales_dict.values())