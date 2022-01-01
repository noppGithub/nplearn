# ====================================== Built-in Function in Python ======================================

# Check the type of object
x = '1'
y = 1
z = 1.1
print(type(x))
print(type(y))
print(type(z))
# =========================================================================================================

# Check length
x = '123'
print(len(x))

x = [1,2,3,4,5,6,7,8,9,10]
print(len(x))
# =========================================================================================================


# str(), int(), float(): change the type of variable
x = '1'
print(type(x))
x = int(x)
print(type(x))
print(type(str(z)))
print(type(float(str(z))))

# =========================================================================================================

# list(),tuple()
x = '123'
x_list = list(x)
x_tuple = tuple(x)
print(x_list)
print(x_tuple)

# =========================================================================================================

# Create a Python dictionary
x = {
    'a' : 1,
    'b' : 2,
    'c' : 'test'
}
print(x)

x = dict(a=1,b=2,c='test')
print(x)

a_list = [('a',1),('b',2),('c','test')]
print(dict(a_list))

a_list = ['a','b','c']
b_list = [1,2,'test']
print(dict(zip(a_list,b_list)))
# =========================================================================================================
# zip: take multiple iterables, pack them as a tuple and return them
index_no = [1,2,3]
names = ['a','b','c']
ages = [10,20,30]

x = list(zip(index_no,names,ages))
print(x)

# Min, Max, Sum
x = [1,2,3,4,5,6,7,8,9,10]
print(min(x))
print(max(x))
print(sum(x))

# =========================================================================================================

# iterate and next
x = [1,2,3]
x_iter = iter(x)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))

# =========================================================================================================
# open(): Write some content to a file, you can also dump JSON to a file.
with open('myfile.txt','w') as f:
    f.write('Hello NpLearn')

# range(): return a list of numbers
x = list(range(10))
print(x)
x = list(range(1,10))
print(x)
x = list(range(0,10,2))
print(x)

# =========================================================================================================

# reversed and sorted
x = [1,2,3]
y = list(reversed(x))
z = list(sorted(y))
print(y)
print(z)

# =========================================================================================================

# round
x = 1.234
y = round(x,1)
print(y)

# =========================================================================================================


# Get input from user
name = input('Please input your name...')
print(f"The input name is {name}")

# =========================================================================================================

# check if the object is match with class
x = 1
print(isinstance(x,int))

# =========================================================================================================

# Filter and Map
# map: apply a given function to the iterable
# filter: return an iterator from input elements wich a function returns True
def my_map_func(num):
    return num + 1

def my_filter_func(num):
    return num < 5

x = [1,2,3,4,5,6,7,8,9,10]
y = list(map(my_map_func,x))
print(y)

z = list(filter(my_filter_func,x))
print(z)

# =========================================================================================================
# Try to get a list of attributes of the input object
x = [1,2,3]
print(dir(x))

print(x.__len__())

print(dir(abs))

def my_func():
    print('Hi')
print(dir(my_func))

# =========================================================================================================
# Get the absolute value of a number
x = 10
print(abs(x))

x = -10
print(abs(x))

# =========================================================================================================

# Return True if `all` elements of the iterable are true
x = [True,True,True]
print(all(x))

x = [False,True,True]
print(all(x))

# Return True if `any` element of the iterable is true
x = [True,True,True]
print(any(x))

x = [False,True,True]
print(any(x))

# =========================================================================================================

# Get a string containing a printable representation of an object
x = 'Gone'
print(ascii(x))

x = 'Göne'
print(ascii(x))
# it can be used on a list as well
x = ['Gone','Göne']
print(ascii(x))

# =========================================================================================================

# Convert an integer number to a binary string prefixed with “0b”
x = 1
print(bin(x))

x = 5
print(bin(x))

x = 10
print(bin(x))

# =========================================================================================================
# Return a Boolean value
x = 'Yes'
print(bool(x))

x = 'No'
print(bool(x))

x = None
print(bool(x))

x = False
print(bool(x))

# =========================================================================================================

# Get `byte` object
x = 1
print(bytes(x))

x = 10
print(bytes(x))

# =========================================================================================================

# Check if the object can be called
x = 1
def a_function():
    print('I am a callable function')
y = a_function

print(callable(x))
print(callable(y))

# =========================================================================================================

# chr: Get the string representing a character whose Unicode code point is the integer
# ord: Get an integer representing the Unicode code point of that character
# chr is the inverse of ord
x = 97
y = 'a'
print(chr(x))
print(ord(y))

# =========================================================================================================

# Get a pair of numbers consisting of their quotient and remainder when using integer division
# 2 * 5 = 10, remain 1
print(divmod(11,2))

# =========================================================================================================

# Return an enumerate object
x = ['a','b','c','d']
print(list(enumerate(x)))

x = ['a','b','c','d']
print(list(enumerate(x,start=1)))

# =========================================================================================================

