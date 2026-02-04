age = int(input("Enter your age: "))

if (age >18):
    print("You can drive a car.")
elif age == 18:   
    print("You can drive a car, but you need to shedule an appointment for a driving test.")
elif age == 0:
    print("You are not born yet.")
else:
    print("You cannot drive a car, you are too young.")