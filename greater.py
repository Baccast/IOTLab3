while True:
    # Get inputs
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")
    num3_input = input("Enter the third number: ")

    # Check if input is a valid int
    if num1_input.isdigit() and num2_input.isdigit() and num3_input.isdigit():
        num1 = int(num1_input)
        num2 = int(num2_input)
        num3 = int(num3_input)
        break
    else:
        print("Invalid input. Please enter a valid integer.")

# Find the greater number
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greater number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greater number.")
else:
    print(f"{num3} is the greater number.")
