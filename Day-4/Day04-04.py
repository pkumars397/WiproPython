class Student:  

    def __init__(self):  
        print("The First Constructor")  

    def __init__(self,name):   # this one is valid 
        self.name=name
        
    def welcome(self):
        print("welcome " , self.name)
  
#st = Student() # so we should give argument ,so error.
st1=Student("Doss")
st1.welcome()


#constructor overloading is not allowed.