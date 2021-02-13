#################################################
# Numpy 1D Array Quick Practice Lab
#################################################

print("QUICK PRACTICE LAB")

# Question 1
# Cast the following list to a numpy array:

import numpy as np
a=[1,2,3,4,5]

# Answer:

np_a = np.array(a)
print(np_a)

# Question 2
# 1) Type using the function type

print(type(np_a))

# Question 3
# 2) The shape of the array

print(np_a.shape)

# Question 4
# 3) The type of data in the array

print(np_a.dtype)

# Question 5
# 4) Find the mean of the array

print(np_a.mean())

#################################################
# Numpy 1D Array Quiz
#################################################

print("QUIZ")

# Question 1
# What is the result of the following operation
# np.array([1,-1])*np.array([1,1])
# Prediction: [1,-1]

print(np.array([1,-1])*np.array([1,1]))

# Question 2
# What is the result of the following operation
# np.dot(np.array([1,-1]),np.array([1,1]))
# Prediction: 0

print(np.dot(np.array([1,-1]),np.array([1,1])))

#################################################
# Numpy 1D Array Lab
#################################################

print("LAB")

# Question 1
# Implement the following vector subtraction in numpy: u-v

u = np.array([1, 0])
v = np.array([0, 1])

# Answer:

print(u-v)

# Question 2
# Multiply the numpy array z with -2:

z = np.array([2, 4])

# Answer:

print(-2*z)

# Question 3
# Consider the list:
# [1, 2, 3, 4, 5]
# and
# [1, 0, 1, 0, 1]
# and cast both lists to a numpy array then multiply them together:

list1 = np.array([1, 2, 3, 4, 5])
list2 = np.array([1, 0, 1, 0, 1])

print(list1*list2)

# Question 4
# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b.
# Then, plot the arrays as vectors using the fuction Plotvec2 and find the dot product:

import matplotlib.pyplot as plt

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.show()

# Answer:

a = np.array([-1, 1])
b = np.array([1, 1])

# Plotvec2(a,b) <- uncomment for graph in solution
print(np.dot(a,b))

# Question 5
# Convert the list [1, 0] and [0, 1] to numpy arrays a and b.
# Then, plot the arrays as vectors using the function Plotvec2 and find the dot product:

a = [1, 0]
b = [0, 1]

print(np.dot(a,b))

# Plotvec2(a,b) <- gives error in this exercise, even in IBM lab environment

# Question 6
# Convert the list [1, 1] and [0, 1] to numpy arrays a and b.
# Then plot the arrays as vectors using the fuction Plotvec2 and find the dot product:

a = [1, 1]
b = [0, 1]

print(np.dot(a,b))

Plotvec2(a,b)