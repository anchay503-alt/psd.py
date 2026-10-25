from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def a(self):
        print("HI")
class cat(Animals):
    def b(self):
        print("cat class")
class Dog(Animals):
    def c(self):
        print("Dog class")
e=cat()
e.b()
d=Dog()
d.c()  

    
