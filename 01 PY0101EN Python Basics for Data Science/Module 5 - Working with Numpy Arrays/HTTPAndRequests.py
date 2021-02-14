#################################################
# HTTP and Requests Lab
#################################################

import requests

import os 
from PIL import Image
from IPython.display import IFrame

# You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)

# We have the response object r , this has information about the request, like the status of the request.
# We can view the status code using the attribute status_code
print(r.status_code)

# You can view the request headers:
print(r.request.headers)

# You can view the request body, in the following line,
# as there is no body for a get request we get a None:
print("request body:", r.request.body)

# You can view the HTTP response header using the attribute headers.
# This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)

# We can obtain the date the request was sent using the key Data
print(header['date'])

# Content-Type indicates the type of data:
print(header['Content-Type'])

# You can also check the encoding:
print(r.encoding)

# As the Content-Type is text/html we can use the attribute text to display the HTML in the body.
# We can review the first 100 characters:
print(r.text[0:100])

# You can load other types of data for non-text requests like images,
# consider the URL of the following image:
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

# We can make a get request:
r=requests.get(url)

# We can look at the response header:
print(r.headers)

# We can we can see the 'Content-Type'
print(r.headers['Content-Type'])

# An image is a response object that contains the image as a bytes-like object.
# As a result, we must save it using a file object.
# First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
print(path)

# We save the file, in order to access the body of the response we use the attribute content
# then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)

# We can view the image:
url_image = Image.open(path)
# url_image.show() <- Uncomment if you wish to open the image

#################################################
# HTTP and Requests Lab Exercises
#################################################

# Exercise 1
print("EXERCISE 1")
# In the previous section, we used the wget function to retrieve content from the web server
# as shown below.
# Write the python code to perform the same task.
# The code should be the same as the one used to download the image,
# but the file name should be 'example.txt'.

# !wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt

# Solution 1:

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

path=os.path.join(os.getcwd(),'example.txt')

with open(path,'wb') as f:
    f.write(r.content)

# Solution 2:

import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
urllib.request.urlretrieve(url, 'example.txt')

with open("example.txt", 'r') as textfile:
    print(textfile.read())