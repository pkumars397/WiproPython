class Animal:
   def speaks(self):
      print("Animals Speaks: ")
#Dog inheritates from Animal
class Dog(Animal):
   def bark(self):
      print("Dog barks")
#DogChild inheritates from Dog
class DogChild(Dog):
    def eat(self):
       print("Eating Bread")

d=DogChild()
d.bark()
d.speaks()
d.eat()

#Its type of Multi Level inheritence