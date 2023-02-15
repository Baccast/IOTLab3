# Get inputs
hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

# Calculate overtime pay
if hours_worked <= 39:
    overtime_pay = 0
elif hours_worked <= 44:
    overtime_pay = (hours_worked - 39) * hourly_rate * 0.5
elif hours_worked <= 49:
    overtime_pay = (5 * hourly_rate * 0.5) + ((hours_worked - 44) * hourly_rate * 0.75)
else:
    overtime_pay = (5 * hourly_rate * 0.5) + (5 * hourly_rate * 0.75) + ((hours_worked - 49) * hourly_rate)

# Print overtime pay
print(f"The overtime pay is ${overtime_pay:.2f}")
