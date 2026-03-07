# Class: Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

#Object: An object is an instance of a class. It is created using the class blueprint and can have its own unique values for the attributes defined in the class.

class Employee:
    company = "Dell"  # Class Attribute

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34226  
    

e = Employee() # An object of class Employee is created here    
print(e.get_salary())  # Employee e's get salary method is called 

e2 = Employee()
print(e2.get_salary())
print(e.company)  # Employee e's company attribute is called