# The super() builtin returns a proxy object (temporary object of the
# superclass) that allows us to access methods of the base class.

# Use of super()
# In Python, super() has two major use cases:

"""
1. Do not need to specify the base class name explicitly, allow us to change the
   base class name without breaking application.
2. Working with Multiple Inheritance
"""


class Human(object):
  def __init__(self, gender):
    print('Human gender:', gender)
    
class Women(Human):
  def __init__(self):
    # call superclass
    super().__init__('Women')
    print(f"created women object")

if __name__ == "__main__":
    alice = Women()
