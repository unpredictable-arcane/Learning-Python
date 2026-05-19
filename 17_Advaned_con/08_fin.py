a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))

try:
    c = a/b
    print(c)

except Exception as e:
    print(e)

finally:
    print("I am always executed")