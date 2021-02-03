############################################
# Objects and Classes Quick Practice Lab
############################################

print("Objects and Classes Quick Practice LAB")

# You will need the class Car for the next exercises.
# The class Car has four data attributes:
# make, model, colour and number of owners (owner_number).
# The method  car_info()  prints out the data attributes.
# The method sell() increments the number of owners.

class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1


# Create a  Car  object my_car with the given data attributes:

make="BMW"
model="M3"
color="red"

my_car = Car(make, model, color)

# Use the method car_info() to print out the data attributes

print(my_car.car_info())

# Call the method  sell()  in the loop, then call the method  car_info() again
# for i in range(5):

for i in range(5):
    my_car.sell()

print(my_car.car_info())

############################################
# Objects and Classes Quiz
############################################

print("Objects and Classes QUIZ")

# Question 1
# Using the Class Car in the lab
# create a Car object with the following attributes:
# make="Honda"
# model="Accord"
# color="blue"

my_car = Car(make="Honda", model="Accord", color="blue")
my_car = Car("Honda","Accord","blue")

print(my_car.car_info())

# Question 2
# From the lab how would you change the data attribute owner_number

# Correct answer:
my_car.sell()

############################################
# Objects and Classes Lab
############################################

print("Objects and Classes Lab EXERCISES")

# Text Analysis
# You have been recruited by your friend, a linguistics enthusiast
# to create a utility tool that can perform analysis on a given piece of text.
# Complete the class 'analysedText' with the following methods -
#
# Constructor - Takes argument 'text'
# makes it lower case and removes all punctuation.
# Assume only the following punctuation is used
# period (.), exclamation mark (!), comma (,) and question mark (?).
# Store the argument in "fmtText"
# 
# freqAll - returns a dictionary of all unique words in the text
# along with the number of their occurences.
# 
# freqOf - returns the frequency of the word passed in argument.
# 
# The skeleton code has been given to you.
# Docstrings can be ignored for the purpose of the exercise.
# Hint: Some useful functions are replace(), lower(), split(), count()

# class analysedText(object):
#
#    def __init__ (self, text):
#        pass
#    
#    def freqAll(self):        
#        pass
#    
#    def freqOf(self,word):
#        pass


class analysedText(object):
    
    def __init__ (self, text):
        text = text.lower()
        text = text.replace('.', '')
        text = text.replace(',', '')
        text = text.replace('?', '')
        text = text.replace('!', '')
        self.fmtText = text
        self.list = text.split()
        pass
    
    def freqAll(self):
        word_dict = {}

        for i, words in enumerate(self.list):
            if self.list[i] not in word_dict:
                word_dict[words] = self.list.count(words)
            else:
                continue
        return word_dict
    
    def freqOf(self,word):
        return self.list.count(word)



# Execute the block below to check your progress.

import sys

sampleMap = {'eirmod': 1,'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1, 'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

print("Constructor: ")
try:
    samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
    print(testMsg(samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
except:
    print("Error detected. Recheck your function " )
print("freqAll: ")
try:
    wordMap = samplePassage.freqAll()
    print(testMsg(wordMap==sampleMap))
except:
    print("Error detected. Recheck your function " )
print("freqOf: ")
try:
    passed = True
    for word in sampleMap:
        if samplePassage.freqOf(word) != sampleMap[word]:
            passed = False
            break
    print(testMsg(passed))
    
except:
    print("Error detected. Recheck your function  " )