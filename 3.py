class Students:
    def __init__(self, name, roll, age):
        self.name = name          
        self._roll = roll         
        self.__age = age         

d = Students("Rahul", 26, 25)

print(d.name)
print(d._roll)
print(d._Students__age)