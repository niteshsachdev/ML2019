"""
Introducing the keywords of OOP

Logically group data and function 
Easy to re-use and build upon
Data and function are known as attributes( characteristics ) 
and methods ( function associated with a class )
class is a blueprint for creating instances 

 
Classes and Instances

Represent Employee in Python 
Individual employee will have specific attributes and methods
Name
email address
Pay

class is a blueprint for creating instances 
each individual employee would be the instance of the class 
"""


"""
Class
"""

class Employee:
    pass



emp_1 = Employee()
emp_2 = Employee()



print ( emp_1)
print ( id(emp_1))


print ( emp_2)
print ( id(emp_2))



"""
Instance variable
"""

# Instance variable has data which is unique to each instance 
# Use __init__ method to create the instance variables ( constructor )
# create init method within the class 

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"


emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print(emp_1.email)
print(emp_2.email)



"""
Methods 
"""

# Adding Action to the class using methods 
# Display Full Name of the employee 
# create method in the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print ( emp_1.fullname() )
print ( emp_2.fullname() )


# calling the methods from the class name, 
# but we need to pass the instance
print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))


"""
Class Variables
"""
# Variables which are shared among all the instance of the class 
# Class variable should be the same for all the instances of the class

# Which are the data which can be shared among all the employees
# class variable that holds the number of employees depending on the instances created 

class Employee:
    # declare this in the class level 
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        # we need to increase the value in the init method
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


print ( Employee.num_of_emps )


"""
Inheritance - Creating Subclasses
"""

class Developer( Employee ) :
    pass

dev_1 = Developer ("Sylvester", "Fernandes",50000)
dev_2 = Developer ("Yogendra", "Singh",60000)

print ( dev_1.email )
print ( dev_2.email )

# This gives a clear picture of the inheritance and the variables 
# Method resolution order
print ( help( Developer ) ) 






"""
What is a Generator?
"""

"""
A generator is a function that behaves like an iterator. 
An iterator loops (iterates) through elements of an object, 
like items in a list or keys in a dictionary. 
A generator is often used like an array, but there are a few differences:

It does not hold results in memory,
It may take longer to run (Trade off using more time for using less space),
It is ‘lazy’: it does not compute results till you need them,
That is, your list is constructed in bits and pieces, 
with each element calculated when you ask for the element.
You can only iterate over them once.
You’ll get a better feel for what generators are as we go through examples in this post.
"""

# How to code a generator
# The first and more tedious way of coding a generator is defining a function 
# that loops over elements in an object and yields elements as it loops.


#Method 1:



def my_generator(my_list):
    print("This runs the first time you call next().")
    for i in my_list:
        yield i*i

input_list =[1,2,3,4,5]
# Full 'list' would be [1, 4, 9, 16, 25]
gen1 = my_generator(input_list)

next(gen1)
# This runs the first time you call next(). <- printout
# 1

next(gen1)
# 4 (since 2*2=4)


# After running out of elements
next(gen1)
# StopIteration
#Yield is used like return, but (1) it returns a generator, 
#and (2) when you call the generator function, 
#the function does not run completely. 
#[1] The function just returns the generator object. 
#Every time you call next() on the generator object, 
#the generator runs from where you stopped before to the next occurrence of yield.


#Method 2:

#The second way of coding generators is similar to that of coding list comprehensions. It’s much more compact than the previous method:

input_list =[1,2,3,4,5]
# Full 'list' would be [1, 4, 9, 16, 25]
gen2 = (i*i for i in input_list)
#When the generator has run out of entries, it will give you a StopIteration exception.

next(gen2)


"""
Regular Expressions
"""

import re
"""
search() versus match()
The match() function checks for a match only at the beginning of the string (by default) 
The search() function checks for a match anywhere in the string.
"""

"""
findAll()
findall(pattern, string, flags=0)
Finds all the possible matches in the entire sequence and 
returns them as a list of strings. Each returned string 
represents one match.
"""
#-------------------------------------
"""
There are methods like start() and end() to know the 
start and end position of matching pattern in the string.
"""


result = re.match(r'Forsk', 'Forsk forsk Summer Bootcamp')

print (result.start())
print (result.end())

result = re.match(r'forsk', 'Forsk forsk forsk Summer Bootcamp')

print (result.start())
print (result.end())

#-------------------------------------

pattern=re.compile('mm')

result=pattern.findall('Forsk Summer Bootcammp')
print (result)
     
#------------------------------------
result=re.findall(r'\w{3}','ForskSummerBootcamp')
print (result)

#to skip blanks
result=re.findall(r'\w+','Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'^\w+','Forsk Summer Bootcamp')
print (result)

#To find end
result=re.findall(r'\w+$','Forsk Summer Bootcamp')
print (result)

result=re.findall(r'\w\w','Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'@\w+\.\w+\.*\w*','abc.test@gmail.com, xyz@test.in, test.first@company.com nimish@gmail.co.in')
print (result)



#-----------------------------------
#find date format numbers
result=re.findall(r'\d{2}-\d{2}-\d{4}','Kunal 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#----------------------------------

li=['+91-7999999999', \
    '399999-999', \
    '99999x9999', '2999999999']


for val in li:
 if re.findall(r'\+?[0-9]{0,2}-?[1-9]{1}[0-9]{9}',val):
     print ('yes')
 else:
     print ('no')




"""
GIT Commands
"""
# Why git and what git can do
# Install git locally and Goto Github and create an account
# Create a new empty remote repo on Github with ForskLabs, which should be Public and click create repository
# copy the HTTPS URL of repo ( https://github.com/neuerung/ForskLabs.git  )
# Goto terminal or Command Prompt and change directory to the desktop 
# git clone https://github.com/neuerung/ForskLabs.git as to clone as a local repo 
# Change directory to FoskLabs
# create a test.py file on desktop/ForskLabs
# git config user.email "sylvester@neuerung.co.in"
# git config user.name "Dr. Sylvester Fernandes"

# Example to understand the concept 
# git add test.py 
# git commit -m "Added new file"
# git status #whether it is nothing to commit
# git push
# Goto github.com and refresh your page to see the test.py


# Onetime Workflow for old files
# Add all the files in the new folder
# git add --all
# git commit -m "Adding all files"
# git status
# git push
# Goto github.com and refresh your page to see all the files


# Everyday Workflow for new files
# git add <filename>
# git commit -m "Added new file"
# git status #whether it is nothing to commit
# git push
# Goto github.com and refresh your page to see all the new file added






