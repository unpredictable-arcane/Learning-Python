def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70 

# a = very_slow_func()
# if (a:= very_slow_func()) > 50:   #Walrus operator
#     print(a)

# else:
#     print("Its not greater than 50")



while(data:=input("Enter the value: ")):
    print(f"You entered {data}")
    if data == "q":
        break