############################################
# Functions Quick Practice Lab
############################################

print("FUNCTIONS QUICK PRACTICE LAB")

# Complete the function  f  so that it returns the product of  a  and  b ,
# use the next cell to test the function
# def f(a,b):
#    
#    return

def f(a,b):
    
    return a*b

# Test the function using the next cell:

a=4
b=2

if a*b==f(a,b):   
    print("correct")   
else:    
    print("incorrect")

# Complete the function  g  such that the input c
# is a list of integers and the output is the sum of
# all the elements in the list
# def g(c):
#
#    return

def g(c):
    return sum(c)

# Test the function using the next cell:

c=[1,2,3,4,5]

if sum(c)==g(c):   
    print("correct")   
else:    
    print("incorrect")

############################################
# Functions Quiz
############################################

print("FUNCTIONS QUIZ")

# Question 1
# What is the value of c after the following block of code is run ?
print("Question 1")

a=1

def add(b):
    return a+b

c=add(10)
print(c)

# Question 2
# What value will be returned after the following block of code is run?
print("Question 2")

def f(c):
    return sum(c)

############################################
# Functions Lab
############################################

print("FUNCTIONS LAB")

# Question 1
# Come up with a function that divides the first input by the second input:
print("Question 1")

def divide(a,b):
    return a/b

# Question 2
# Use the function con for the following question.

def con(a, b):
    return(a + b)

# Can the con function we defined before be used to add two integers or strings?
print("Question 2")

print(con(5,3))
print(con("Hej","hej"))

# Question 3
# Can the con function we defined before be used to concatenate lists or tuples?
print("Question 3")

print(con([1,2],[3,4]))
print(con((1,2),(3,4)))

# Question 4: Probability Bag
# See "Functions_Quiz_Question_4.txt" for the actual question.
print("Question 4")

def fillBag(**balls):
    global bag
    bag = balls
    pass
     

def totalBalls():
    return sum(bag.values())
    
def probOf(color):
    return(bag[color]/totalBalls())

def probAll():
    probs = {}
    for colors in bag:
        probs[colors] = probOf(colors)
    return probs

# Run this snippet of code to test your solution.

testBag = dict(red = 12, blue = 20, green = 14, grey = 10)
total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")



print("totalBalls : ")
try:
    print(testMsg(total == totalBalls()))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probOf")
try:
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False
        
    print(testMsg(passed) )
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probAll")
try:
    print(testMsg(probAll() == prob))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")