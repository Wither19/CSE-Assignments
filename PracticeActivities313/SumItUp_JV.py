# Inputs to get the addends
first = input("What is the first number? ")
second = input("What is the second number? ")

# Convert the variables to ints
first = int(first)
second = int(second)

# Initialize result to 0
result = 0

# If the two addends are equal, double their sum. If not, add normally
if (first == second):
    result = first * 2 + second * 2
else:
    result = first + second
    
# Change the result of the addition to a string, then print it to the user
result = str(result)
print("your total is:", result)