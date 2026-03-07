class Employee:

    def __init__(self, salary, bond, name): # constructor
        self.salary = salary # Create an instance attribute of name salary and assign it the value of the parameter salary
        self.bond = bond
        self.name = name

    def get_salary(self): 
        return self.salary  # Method to return the salary of the employee object
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The Bond is for {self.bond} years.")
    

e1 = Employee(34567,2,"John Doe") # An object of class Employee is created here with salary 34567 and bond 2 years
# print(e1.get_salary())  # Employee e1's get salary method is called
e1.get_info()