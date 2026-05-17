class Animal: # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal): # Child class (subclass)
        def speak(self):
                super().speak()
                print("Woof! Woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
# print(d.Location) # Accessing the inherited attribute