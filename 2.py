class animals:
    def sound(self):
        print("this is animal class")
class Dog(animals):
    def sound(self):
        print("this is Dog class")
class cat(animals):
    def sound(self):
        print("cat class")
d=Dog()
d.sound()
c=cat()
c.sound()

