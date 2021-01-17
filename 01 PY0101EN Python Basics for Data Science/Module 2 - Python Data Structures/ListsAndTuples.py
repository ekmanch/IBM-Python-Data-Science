# create the Tuple  (0,1,2,3)  and assign it to the variable  A :

A = (0,1,2,3)

# Find the first two elements of the Tuple  A :

print(A[0:2])

# For the next few questions, you will need the following list:

B=["a","b","c"]

# Find the first two elements of the list  B:

print(B[0:2])

# Change the first element of the list to an uppercase  "A" 

B[0] = "A"

print(B)

# Now, let us create your first tuple with string, integer and float.

# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created

type(tuple1)

# We can print out each value in the tuple:

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# We can print out the type of each value in the tuple:

# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# We can obtain the last element as follows (this time we will not use the print statement to display the values):

# Use negative index to get the value of the last element

tuple1[-1]

# We can display the next two elements as follows:

# Use negative index to get the value of the second last element

tuple1[-2]

# Use negative index to get the value of the third last element

tuple1[-3]

# We can concatenate or combine tuples by using the + sign:

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2

# We can slice tuples, obtaining new tuples with the corresponding elements:

# Slice from index 0 to index 2

tuple2[0:3]

# We can obtain the last two elements of the tuple:

# Slice from index 3 to index 4

tuple2[3:5]

# We can obtain the length of a tuple using the length command:

# Get the length of tuple

len(tuple2)

# Sorting

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# We can sort the values in a tuple and save it to a new tuple:

# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted

# A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements:

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples

NestedT[2][1][0]

# Print the second element in the second nested tuples

NestedT[2][1][1]

# Similarly, we can access elements nested deeper in the tree with a fourth index:

# Print the first element in the second nested tuples

NestedT[4][1][0]

# Print the second element in the second nested tuples

NestedT[4][1][1]

# Quiz on Tuples

# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

# Find the length of the tuple, genres_tuple:

print(len(genres_tuple))

# Access the element, with respect to index 3:

print(genres_tuple[3])

# Use slicing to obtain indexes 3, 4 and 5:

print(genres_tuple[3:6])

# Find the first two elements of the tuple genres_tuple:

print(genres_tuple[0:2])

# Find the first index of "disco":

print(genres_tuple.index("disco"))

# Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):

C_tuple=(-5, 1, -3)

print(sorted(C_tuple))