# Inputs for all three numbers (supports floats)
first = input("Enter the first number: ")
second = input("Enter the second number: ")
third = input("Enter the third number: ")

# Convert all user inputs to floats
first = float(first)
second = float(second)
third = float(third)

# Making a variable "formula" to hold the total's division

formula = (first + second + third) / 2

msg = ""

if (formula < 10):
    msg = "This is a small number."

elif (formula >= 10 and formula < 50):
    msg = "Double digits, mid-way."

elif (formula >= 50):
    msg = "Double digits - mature."

# Output string to format
output = "({} + {} + {}) / 2... {} {}"

print(output.format(str(first), str(second), str(third), str(round(formula, 2)), msg))