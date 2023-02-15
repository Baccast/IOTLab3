# Get inputs
points = float(input("Enter the number of points earned: "))
total = int(input("Enter the total number of points possible: "))

# Calculate percentage
percentage = (points / total) * 100

# Assign grade based on percentage
if percentage >= 80:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'E'

# Print standardized grade
print(f"The standardized grade is {grade}")
