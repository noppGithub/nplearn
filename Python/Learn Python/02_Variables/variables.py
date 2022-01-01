"""
Variables is use for storing data in a computer memory, as the name said "vary-able".
the data in a variable can be changed from time to time. 
it's bound to an address in your computer memory.

Best practice:
- use snake_case: all lower-case with underscore to help readability.
- do not start your variable name with number
- it's case-sensitive, you will be fine if you use snake_case 

TDLR; you have to use it, but don't need to remember it :)
"""

my_name = 'nplearn'
my_age = 10
is_single = False
print(my_name,my_age,is_single)

# multiple variable in one line
my_name,my_age,is_single = 'nplearn',10,False
print(my_name,my_age,is_single)

# notice the variable type, learn more in next chapters
print(type(my_name))
print(type(my_age))
print(type(is_single))