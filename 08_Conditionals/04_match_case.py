a = int(input("Enter a number between 1 and 10: "))

match a:
    case 3:
        print("You won a charger!")
    case 5:
        print("You won $30!")
    case 7:
        print("You won a gift card!")
    case _:
        print("Better luck next time!")  # Default case if no match found