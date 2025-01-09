class Base:
    def m1(self):
        print("This is a public method.")

class Derived(Base):
      pass

obj = Derived()
obj.m1()  # Accessible