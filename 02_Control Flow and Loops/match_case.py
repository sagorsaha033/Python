a = int(input("Enter a number between 1 to 10: "))

match a:
    case 1:
        print("You won a phone")
    case 5:
        print("You won a headphone")
    case 9:
        print("You won a laptop")
    case _:
        print("Better luck next time!")