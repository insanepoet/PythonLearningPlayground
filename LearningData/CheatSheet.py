

# Style is off for most of this as it is just a cheat sheet Keep your PEP guidelines outta here
print("HelloWorld")

'''
  NUMBERS
'''

# Basic math is directly interpreted no need to define
5 + 5

# Interpreter will supply a floating point if a floating point is used in a calculation
5 + 5.5

# Supplying a string to int modifies the type
int("5") + int("5")

'''
#  STRINGS
'''

# Single or Double Quotes are fine escaping done via \
print('He told me "You shouldn\'t Forget to escape quotes"')

# Concatenation is done via +
print("Hello " + "World")

# Supplying an integer to str modifies the type
print("This is Line " + str(10 + 17) + "of the file.")

# Split Function can break strings into an array (lists)
"Hello, Dave".split(",")

# Arrays (lists) are zero based
print("Your name is " + "Hello, Dave".split(",")[1])

'''
# BOOLEANS
'''

# Python uses capitalized True and False
5 == 5
5 == 4

# Python understands is and is not can also literal compare strings
5 is 5
5 is not 4
"This" is not "That" # Literal comparison of string
"This" is str(This) # Convert boolean to string

'''
#  LISTS (Arrays)
'''

# Lists can be generated with [ , ]
myarray = ["Movies","Games","Python",str(42)]
print(myarray[2])

# appending to a list .append()
myarray.append("Duke")

# removing from array del, remove(), or pop()
del myarray[4] # remove item in position x
myarray.remove("Python") # remove literal from array
myarray.pop(1) # remove item in position x

# modifying elements of an array
myarray[0] = "Hiking"

'''
 Dictionaries (Json like structures)
'''

# Dictionaries use {} as their definer
mydictionary = {"name": "Nick", "age": 27, "hobby": "Programmer"}
print(mydictionary["name"])

'''
  VARIABLES
'''

# Variables can overwrite themselves (Who would have guessed)
greeting = "Hello World"
greeting = greeting.split(" ")[0]
print(greeting + "Bob")

#

'''
 FUNCTIONS
'''

# str / int / bool
str(5)
int("5")
bool("True")

# len - Determine lengths
len("Hello")
len([1,2,3,4,5])

# sort / sorted - sort arrays
sorted([6,3,4,9,8,7,1,2,5]) #default is low to high
sorted(["A","b","C","d","1","1,3"]) # Num/Float/Caps/Lower

# Functions are defined with def and underscore spaces in their names "Snake Case"
def my_function():
    # Indent 4 spaces, all code following will be considered part of this function
    print("This is a Function!")
# Indent ends so python assumes the function is closed
my_function()

# Arguments and their uses in a function
def second_function(str1,str2): # arguments are passed just like javascript
    print(str1 + " " + str2)
second_function("It", "Works")

# Default Arguments are overwritten by passed arguments
def print_something(name = "hidden", age = "unknown"):
    print("My name is", name, "and my age is", age)
print_something("Bob") # Only good for the first argument
print_something(None,30) # None = Null and can be used to skip the first argument

# arguments can be tied to keywords
def print_somethingelse(name = "hidden", age = "unknown"):
    print("My name is", name, "and my age is", age)
print_somethingelse(age="20", name="Bob")

# Flexible arguments (Infinite) can be used by prefacing the argument as an array with *
def print_people(*people): # *arrayname (arrayname can be used in the function)
    for person in people:
        print("This person is", person)
print_people("Nick", "Dan", "Jack", "Sam", "King", "Smiley")

# Returning Values from functions with return
def do_math(num1, num2):
    return num1+num2
print(do_math(5, 7))

# If, Elif, else statements
check = False
if check == False:
    print("It's False")
elif check == str:
    print("Why you put string in my bool")
elif check == int:
    print("Waiter! There's a num in my bool!")
else:
    print("It's actually True")

# For / While Loops - as you would expect (break, continue)
this_array = [1, 2, 3, 4, 5]
run = True
current = 1

for item in this_array:
    print("Array location", this_array.index(item), "contains", item)

while run:
    if current == 10:
        run == False
    else:
        print(current)
        current += 1

'''
 LIBRARIES / MODULES
'''

# import regex
import re  # Should be at the top
reg_string = "'I AM NOT YELLING', she said. Though we knew it not to be true."
regex_string = re.sub('[A-Z]', '', reg_string)
print(regex_string)

# module imports
from MyModule import fo, bar, foobar

# Importing Modules from rel
# MUST HAVE __init__.py in "class" directory to tell python to load the directory on initiation
from classes.myclass import MyClass  # from directory.filename import ClassIWantToImport

'''
  Classes / Objects
'''

class test:
    atkl = 5
    atkh = 15

    def getAtk(self):
        print(self.atkl)

baddy1= test()  # Create object from test class
baddy1.getAtk()  # perform function from object

class Enemy:

    def __init__(self, atkl, atkh):  # Set instance variables of classes generated on creation of object
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

baddy2 = Enemy(40, 60)
baddy2.getAtk()

baddy3 = Enemy(75, 90)
baddy2.getAtk()