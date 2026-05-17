class Employee:
    def __init__(self, name, salary, projects=0):
        self.name = name
        self._salary = salary  # Protected attribute
        self.projects = projects  # Optional: assign projects

    @property
    def first_name(self):
        parts = self.name.split(" ")
        return parts[0]
    
    @first_name.setter
    def first_name(self, first):
        parts = self.name.split(" ")
        if len(parts) > 1:
            new_name = f"{first} {parts[1]}"
        else:
            new_name = first
        self.name = new_name
    
e = Employee("Anuj kumar", 100000)
# print(e.first_name())  # Wrong way to get property
# e.set_first_name("Aryan")  # Wrong way to set property
 
print(e.first_name)      # Correct way to get property
e.first_name = "Anuj"   # Correct way to set property
print(e.name)