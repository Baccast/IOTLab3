while True:
    # Get year input
    year_input = input("Enter a year: ")
    
    # Check if the input is a valid integer
    if year_input.isdigit():
        year = int(year_input)
        break
    else:
        print("Invalid input. Please enter a valid integer.")

# Check if the year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("True")
else:
    print("False")
