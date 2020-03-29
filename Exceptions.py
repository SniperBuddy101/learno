# Working with exceptions
# Taking a valid integer input from the user

while True:
    try:
        message = int(input("Please enter the number: "))
        break
    except ValueError:
        print("Only enter a number. Nothing else")

print("Done..")
