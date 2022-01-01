class Human(object):
    def __init__(self, Human):
        print(Human, 'is a type of Human')

class Women(Human):
    def __init__(self,type_name):
        print(type_name,'is a type of Women')
        super().__init__(type_name)

class CuteWomen(Women):
    def __init__(self,CuteWomen):
        print(CuteWomen, 'is so cute.')
        super().__init__(CuteWomen)

class BeautifulWomen(Women):
    def __init__(self,BeautifulWomen):
        print(BeautifulWomen, 'is very beautiful')
        super().__init__(BeautifulWomen)

class GirlFriend(CuteWomen, BeautifulWomen):
    def __init__(self,girlfriend_name):
        print(girlfriend_name,'This is my girlfriend')
        # this will call both CuteWomen and BeautifulWomen
        super().__init__(girlfriend_name)

if __name__ == "__main__":
    ada = GirlFriend(girlfriend_name='Ada')
    print('='*50)
    alice = CuteWomen('Jill')
    
    # Method Resolution Order (MRO)
    a = GirlFriend.mro()
    for item in a:
        print(item)
