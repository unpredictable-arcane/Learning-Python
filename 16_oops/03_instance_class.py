class Employee:
    company = "Asus"  # Class Attribute

    def __init__(self, salary, bond, name,company): # constructor
        self.salary = salary # Create an instance attribute of name salary and assign it the value of the parameter salary
        self.bond = bond
        self.name = name
        self.company = company

    def get_salary(self): 
        return self.salary  # Method to return the salary of the employee object
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The Bond is for {self.bond} years.")
    
e1 = Employee(34567, 2,"John", "Google")
print(e1.company) # prints instance attribute company
print(Employee.company) #This willl always print the class attribute 

# Object introspection
print(dir(e1))