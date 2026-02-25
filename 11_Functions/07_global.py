def sum(a, b):
    print("Hey I am doing the sum")
    c = a + b
    global z # z is a global variable
    z = 0  # z is a local variable which is not accessible outside this function
    return c

z = 9  # z is a global variable
print(sum(3, 11))
print(z)