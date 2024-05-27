name = input("Name: ")
print("Hello there,", name,"let's crack some Math equations!")
print("Choose which operator you would like to use in the following options provided below.")

#start by defining the symbols for the calculator ( +, x , / , -)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def multiply(x, y):
    return x * y

def exponent(x, y):
    return x ** y

# Create a menu for user interaction

def menu():         #<<<<This function prints the options available for the user to choose from.>>>
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponents")

while True: #this "while True" loop causes the code to run indefinetely until it encounters a break statement.
    menu()

    choice = input("Enter choice (1, 2, 3, 4, 5): ")
    if choice > '5':
        print("Hey there,",name,"you can only choose between Options 1 - 5")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        elif choice == '5':
            print(f"{num1} ** {num2} = {exponent(num1, num2)}")
        else:
            print("Invalid User Input")

    next_calculation = input("Would you like to peform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break 

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(name,"this is Invalid input! Please enter a number.")
        continue
