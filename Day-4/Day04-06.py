class Student:    
    def __init__(self,name,id,age):  
  
        self.name = name   
        self.id = id  
        self.age = age    

    def display_details(self):  
  
        print("Name   " , self.name)
        print("Id     " , self.id)
        print("Age    " , self.age)
    
s = Student("John",101,22)
  
print(s.__dict__)
print(s.__module__)