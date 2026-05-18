# while True:
#     try:

#        a = int(input("Enter a number 1: "))
#        b = int(input("Enter a number 2: "))
#        print(f"The division is {a/b}")

#     except ValueError:
#         print("Please don't perform bad typecasts")

#     except ZeroDivisionError:
#         print("MAT KAR LALA zero se divide mat kar")

#     except Exception as e:
#          print("Unknown Error occurred!", e)

a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

if b == 0:
    raise ValueError("pleade don't divide by zero")
print(f"The division is {a/b}")

      