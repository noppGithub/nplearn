class NPLearn(object):
    def __init__(self,firstname,height,weight):
        self.__version__ = '2021.07.04'
        self.var1 = firstname
        self.var2 = height
        self.var3 = weight
        self.age = 5

    def print_me(self):
        print("My firstname is {}, I am {} years old with {} height and {} weight".format(self.var1,self.age,self.var2,self.var3))

if __name__ == "__main__":
    npl = NPLearn(firstname=1,height=2,weight=3)
    npl.print_me()
    npl.age = 30
    npl.print_me()
 