#Decorator is a function that takes a function,it creates a new function inside its body (wrapper). Then it returns that new function.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper



@my_decorator  #Decorator is called here
def say_hello():
    print("Hello!")

# say_hello()
# f = my_decorator(say_hello)  #Decorator is called here
# f()

'''

f will look somthing like this:

 def f():
        print("Something is happening before the function is called.")
        print("Hello!")
        print("Something is happening after the function is called.")
'''