class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self._salary}"
    
    def __repr__(self):
        return f"Employee('{self.name}', {self._salary})"
    
    def __len__(self):
        return len(self.name)

e = Employee("Anuj",100009)
print(len(e))
# print(e.name, e._salary)
# print(str(e))
# print(repr(e))