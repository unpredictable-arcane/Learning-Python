def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1 # z is a local variable which is not accessible outside this function
    return c

def greet():
    z = 5 # z is a local variable in this function
    print("Hello, World!")

z = 9 # z is a global variable
print(z)
print(sum(3, 4))
print(z)