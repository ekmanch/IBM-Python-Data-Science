######################################
# Sets Lab
######################################

# Cast the following list to a set:

print(set(['A','B','C','A','B','C']))

# Add the string 'D' to the set S

S={'A','B','C'}
S.add('D')
print(S)

# Find the intersection of set A and B

A={1,2,3,4,5}
B={1,3,9, 12}

print(A & B)

######################################
# Sets Quiz
######################################

# Question 1:
# What is the result of the following lines of code:

S={'A','B','C'}

U={'A','Z','C'}

print(U.union(S))

# Question 2:
# What is the intersection of set S and U

S={'A','B','C'}

U={'A','Z','C'}

print(S&U)

######################################
# Sets in Python Lab - Quiz Part
######################################

# Question 1
# Convert the list ['rap','house','electronic music', 'rap'] to a set:

print(set(['rap','house','electronic music', 'rap']))

# Question 2
# Consider the list A = [1, 2, 2, 1]
# and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

# Answer will be no as sets do not include duplicates.
# Set will be 1+2 = 3, while list will be 1+2+2+1 = 6.

print('Sum A = ', sum(A))
print('Sum B = ', sum(B))

# Question 3
# Create a new set album_set3 that is the union of album_set1 and album_set2:

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)

print(album_set3)

# Question 4
# Find out if album_set1 is a subset of album_set3:

print(album_set1.issubset(album_set3))