class Base:
    def __init__(self):
        self._protected_attr="Protected"
    def protected_method(self):
        print("This is protected Method")
        
class Derived(Base):
     pass
obj=Derived()
print(obj._protected_attr)
obj.protected_method()