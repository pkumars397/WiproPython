class Base:
    def __init__(self):
        self.__age=45  #two underscore for private data member
    def __m1(self): #private method (two underscore)
        print("this is private method")
        
class Derived(Base):
    pass
obj=Derived()
print(obj._age)
obj.__m1()