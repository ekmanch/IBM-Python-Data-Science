################################################################
# Tuples Lab
################################################################

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

################################################################
# Lists Lab
################################################################

# Create a list

L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# Lists can contain strings, floats, and integers. We can nest other lists
# and we can also nest tuples and other data structures.
# The same indexing conventions apply for nesting:

# Sample List

print(["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)])

# We can also perform slicing in lists.
# For example, if we want the last two elements, we use the following command:

# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
print(L)

# List slicing

print(L[3:5])

# We can use the method extend to add new elements to the list:

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# Another similar method is append.
# If we apply append instead of extend, we add one element to the list:

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)

# Each time we apply a method, the list changes.
# If we apply extend we add two new elements to the list.
# The list L is then modified by adding two new elements:

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# If we append the list ['a','b']
# we have one new element consisting of a nested list:

# Use append to add elements to list

L.append(['a','b'])
print(L)

# As lists are mutable, we can change them.
# For example, we can change the first element as follows:

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# We can also delete an element of a list using the del command:

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

# We can convert a string to a list using split.
# For example, the method split translates
# every group of characters separated by a space into an element in a list:

# Split the string, default is by space

print('hard rock'.split())

# We can use the split function to separate strings on a specific character.
# We pass the character we would like to split on into the argument
# which in this case is a comma.
# The result is a list, and each element corresponds to a set of characters
# that have been separated by a comma:

# Split the string by comma

print('A,B,C,D'.split(','))

# When we set one variable B equal to A;
# both A and B are referencing the same list in memory:

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Initially, the value of the first element in B is set as hard rock.
# If we change the first element in A to banana, we get an unexpected side effect.
# As A and B are referencing the same list,
# if we change list A, then list B also changes.
# If we check the first element of B we get banana instead of hard rock:

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# You can clone list A by using the following syntax:

# Clone (clone by value) the list A

B = A[:]
print(B)

# Now if you change A, B will not change:

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

################################################################
# Lists Quiz
################################################################

# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.

a_list = [1, 'hello', [1,2,3], True]
print(a_list)

# Find the value stored at index 1 of a_list.

print(a_list[1])

# Retrieve the elements stored at index 1, 2 and 3 of a_list.

print(a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:

A = [1, 'a']
B = [2,1,'d']

# A.extend(B)

print(A + B)