class Employee:
    def __init__(self,name,salary,password):
        self.name=name          
        self._salary=salary        
        self.__password=password       

c=Employee("Prem",1000000, "Prem@123")

print("Name:",c.name)
print("Sallary",c._salary)
print("Password",c._Employee__Password)