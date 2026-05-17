class Employee:
    company = "Google"  # Static/Class variable
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    
    # Instance method
    def print_info(self):
        info = (f"Name: {self.name}, Salary: {self._salary}, Company: {Employee.company}")
        print(info)

    # Static method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Add this method
    def print_company(self):
        print(self.company)

e1 = Employee("Anuj", 100000)
e2 = Employee("Aryan", 200000)

# print(Employee.company)
# print(Employee.name)  # Error: class has no attribute 'name'
# e1.print_info()
# e2.print_info()



print(Employee.company)
e1.change_company("Amazon")
print(Employee.company)