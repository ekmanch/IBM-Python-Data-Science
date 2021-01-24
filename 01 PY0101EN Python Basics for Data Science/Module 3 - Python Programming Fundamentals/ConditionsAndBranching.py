############################################
# ConditionsAndBranching Quick Practice Lab
############################################

# Find the value of i that produces a True
# i = ?
# i!=0
i=1
print(i!=0)

# Find the value of x that prints the statement: "this is a"
# x = ?
# if(x=='a'):
#    print("this is a")
# else:
#     print("this is  not a")
x='a'
if(x=='a'):
    print("this is a")
else:
    print("this is  not a")

# find the value of y that produces a True statement
# y=
# x=1
# x>0 and y<10
y=9
x=1
print(x>0 and y<10)

############################################
# ConditionsAndBranching Quiz
############################################

# Question 1
# Find the values of i that produces a True for the following:
# i!=0
# Possible answers: 1, 0, -1, 10000000

i = 1
print("Question 1, Answer 1: ", i!=0)

i = 0
print("Question 1, Answer 2: ", i!=0)

i = -1
print("Question 1, Answer 3: ", i!=0)

i = 10000000
print("Question 1, Answer 4: ", i!=0)

# Question 2
# What is the output of the following:
# x='a'
# if(x!='a'):
# print("this is not a")
# else:
# print("this is a")

x='a'
if(x!='a'):
    print("this is not a")
else:
    print("this is a")
    
############################################
# ConditionsAndBranching Lab
############################################

# Question 1
# Write an if statement to determine if an album had a rating greater than 8.
# Test it using the rating for the album “Back in Black”
# that had a rating of 8.5.
# If the statement is true print "This album is Amazing!"

album = 8.5

if (album > 8):
    print("This album is Amazing!")

# Question 2
# Write an if-else statement that performs the following.
# If the rating is larger then eight print “this album is amazing”.
# If the rating is less than or equal to 8 print “this album is ok”.

if (album > 8):
    print("This album is Amazing!")
else:
    print("This album is ok")

# Question 3
# Write an if statement to determine if an album came out before 1980
# or in the years: 1991 or 1993.
# If the condition is true print out the year the album came out.

release_year = 1993

if (release_year < 1980) or (release_year == 1991) or (release_year == 1993):
    print("The album was released in: ", release_year)