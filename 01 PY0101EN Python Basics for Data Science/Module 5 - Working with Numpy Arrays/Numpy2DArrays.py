#################################################
# Numpy 2D Arrays Quick Practice Lab
#################################################

# You will use the numpy array  A for the following
import numpy as np
A=np.array([[11,12],[21,22],[31,32]])

# Question 1:
# 1) Type using the function type

print(type(A))

# Question 2
# 2) The shape of the array

print(A.shape)

# Question 3
# 3) The type of data in the array

print(A.dtype)

# Question 4
# 4) Find the second row of the numpy array A:

print(A[1,:])

# You will use the following numpy arrays for the next questions:
A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

# Question 1
# 1) Multiply array  A  and B

print(A*B)

# Question 2
# 2) Perform matrix multiplication on array  A and  B (order will not matter in this case)

print(np.dot(A,B))

#################################################
# Numpy 2D Arrays Quiz
#################################################

print("QUIZ")

# Question 1
# How many rows is the following numpy array?

A=np.array([[1,2],[3,4],[5,6],[7,8]])

# Prediction: 4,2 array, 4 rows, 2 columns

print(A.shape)

# Question 2
# How can you perform the following operation?
# np.dot(A,B)

A=np.array([[1,2],[3,4],[5,6],[7,8]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])

# Prediction: You can't. They don't have the correct dimensions (A is 4,2 and B is 3,3)

# np.dot(A,B) <- Uncomment to see error message when running script

#################################################
# Numpy 2D Arrays Lab
#################################################

print("LAB")

# Question 1
# Consider the following list a, convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

a = np.array(a)

# Question 2
# Calculate the numpy array size.

print(a.size)

# Question 3
# Access the element on the first row and first and second columns.

print(a[0][0:2])

# Question 4
# Perform matrix multiplication with the numpy arrays A and B.

b = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])

# Answer:

print(np.dot(a,b))