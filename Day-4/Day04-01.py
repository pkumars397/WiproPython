class Person:
   def __init__(self,n,a):  # constructor will executed automatically when create object
       self.name=n
       self.age=a
   def greet(self):
       print(f'My name is {self.name} and age is {self.age}')


person1=Person("Prashant",24)
person2=Person("binu",26)
person1.greet()
person2.greet()