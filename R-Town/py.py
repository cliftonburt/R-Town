https://docs.python.org/3/library/stdtypes.html

# Built-in Functions
https://docs.python.org/3/library/functions.html

abs() #Takes in a numeric data type such as int or float and returns the absolute value of the argument

all() # Returns True if every item in an iterable evaluates to True, otherwise, it returns False

any() #Takes in an iterable object such as a list or tuple and returns True if any of the elements in the iterable are true. If none of the elements present in the iterable are true, any() will return False.

ascii() # Receives as input an object containing string data, and returns the object as a printable representation with escapes for non-ASCII characters (accented characters)

bin() #converts an integer into its binary equivalent string

bool() #Converts a value to a Boolean True or False value

breakpoint() # Engage, configure, and change the debugger program used in a script

bytearray() #Returns an array of the given bytes of an object

bytes() # Returns a byte immutable object representing the given bytes of an object

callable() # Returns True if an object is callable, and False if an object is not callable

chr() #Returns Unicode characters represented by integers ranging between 0 and 1,114,111

classmethod() #Converts a given function into a class method

compile() # Returns a runnable code object created from a string

complex() # Converts a given string into a complex number

delattr() # Allows the user to delete attributes from an object

dict() # Initializes a new dictionary from mapping n-number of onject (key, value) pairs

float() # Takes in a numeric, string, or no value and a copy of that value in the floating point data type

input() # Takes in a value from the user an converts the value into a string

int() # Take in a value that can be converted into an integer, a returns a copy of the value in the int datatype

max() # Returns the highest value from values given or an iterable

min() # Returns the lowest value from values given or iterable

pow() # Returns the value of a base number x to the power of an exponent y, with an optional modulus z

reversed() # Takes in an iterator object, such as a list or string, and returns a reversed iterator object

round() # Takes a number and an integer as parameters, and returns the number with decimal places equal to the integer

sorted() # Takes in an iterator object, such as a list, dictionary, set, or string, and sorts it according to a parameter

zip() # Takes multiple iterators as input and returns a single zip object made up of a list of tuples 

----

# FUNCTIONS

# Define a function my_function() with parameter x
def my_function(x):
    return x + 1
    
    # Invoke the function
    
    print(my_function(2))
    print(my_function(3 + 5))
    
    
# A function can be called by writing the name of it, followed by parentheses.

doHomework()


# Check for leap year and return a string indicating if it is or not

def check_leap_year(year):
  if year % 4 == 0:
    return str(year) + " is a leap year"
  else:
    return str(year) + " is not a leap year"

year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) 
    

# Variable scope. Global vs. local scope at work at the example below:

a = 5
 
def f1():
  a = 2
  print(a)
  
print(a)   # Will print 5
f1()       # Will print 2
    
    
# PROBABILITY DISTRIBUTIONS

import scipy.stats as stats
import numpy as np

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 6)
print(np.random.choice(die_6, size = 5, replace = True))


## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))


## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))


## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))


## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))


# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))





    