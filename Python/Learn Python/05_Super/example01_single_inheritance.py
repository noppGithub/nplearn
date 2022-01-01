class Human(object):
  def __init__(self, type_name):
    print(type_name, 'is a type of Human')
    
class Women(Human):
  def __init__(self):
    print('Women has 2 arms')
    super().__init__('Women')

# ============== change the base class without changing code =================
# class Mammal(object):
#   def __init__(self, type_name):
#     print(type_name, 'is a type of Mammal')

# class Women(Mammal):
#   def __init__(self):
#     print('Women has 2 arms')
#     super().__init__('Women')

if __name__ == "__main__":
    an_object = Women()