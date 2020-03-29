while True:
    try:
        the_number = int(input("Enter the number"))
        break
    except ValueError:
        print("Please enter a valid number")
if the_number > 30:
    print("The temperature is high! It's hot!")
elif the_number > 20:
    print("It's fine. Neither cool nor hot. Just Chill.")
else:
    print("It's cold!!")
