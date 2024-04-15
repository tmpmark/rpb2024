def add(x, y):
    return x + y

def main():
    print("This is a calculator")
    print("Choose your operator as a number (1=add, 2=minus, 3=multiply, 4=divide)")
    opttype = int(input("> "))

    # Check the operator chosen and print the corresponding message
    if opttype == 1:
        print("You chose addition.")
    elif opttype == 2:
        print("You chose subtraction.")
    elif opttype == 3:
        print("You chose multiplication.")
    elif opttype == 4:
        print("You chose division.")
    else:
        print("Invalid choice. Please enter a valid number (1-4).")
    print ("Now choose two numbers for x and y")
    x = int (input ("x > "))
    y = int (input ("y > "))
    if (opttype == 1):
        z=add (x, y)
        print ("%d+%d=%d" % (x,y,z))


# Call the main function to run the calculator
if __name__ == "__main__":
    main()

