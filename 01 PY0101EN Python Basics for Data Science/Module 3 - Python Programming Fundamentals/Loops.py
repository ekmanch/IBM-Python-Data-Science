############################################
# Loops Quick Practice Lab
############################################

# Use loops to print out the elements in the list A
# A=[3,4,5]

print("QUESTION 1")

A=[3,4,5]

for i in A:
    print(i)

# Find the value of  x  that will print out the sequence  1,2,..,10 
# x=
# y=1
# while(y != x):
#     print(y)
#     y=y+1

print("QUESTION 2")

x=11
y=1
while(y != x):
    print(y)
    y=y+1

############################################
# Loops Quiz
############################################

print("QUIZ")

# Question 1
# what is the output of the following lines of code:

A=[3,4,5]

for a in A:
    print(a)

# Answer prediction: 3\n4\n5

# Question 2
# what is the output of the following lines of code:

x=3
y=1

while(y!= x):
    print(y)
    y=y+1

# Answer prediction: 1\n2

############################################
# Loops Lab
############################################

# Question 1
# Write a for loop the prints out all the elements
# between -5 and 5 using the range function.

print("LAB QUIZ QUESTION 1")

for i in range(-5,6):
    print(i)

# Question 2
# Print the elements of the following list:
# Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
# Make sure you follow Python conventions.

print("LAB QUIZ QUESTION 2")

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for i in Genres:
    print(i)

# Question 3
# Write a for loop that prints out the following list:
# squares=['red', 'yellow', 'green', 'purple', 'blue']

print("LAB QUIZ QUESTION 3")

squares=['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)

# Question 4
# Write a while loop to display the values of the Rating of
# an album playlist stored in the list PlayListRatings.
# If the score is less than 6, exit the loop.
# The list PlayListRatings is given by:
# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

print("LAB QUIZ QUESTION 4")

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i=0

while (i < len(PlayListRatings)) and (PlayListRatings[i] > 3):
    print(PlayListRatings[i])
    i+=1

# Question 5
# Write a while loop to copy the strings 'orange' of the list squares
# to the list new_squares.
# Stop and exit the loop if the value on the list is not 'orange':

print("LAB QUIZ QUESTION 5")

squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []

i=0

while (i < len(squares)) and (squares[i] == 'orange'):
    new_squares.append(squares[i])
    print(new_squares[i])
    i+=1