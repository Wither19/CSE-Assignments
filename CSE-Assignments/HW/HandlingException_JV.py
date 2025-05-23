# Try is code that is executed normally
# Except is code when an error happens
# Else is code when an error doesn't happen
# Finally always executes.

# while (True):
#   # Conversion to an int is the normal response
#   try:
#     answer = int(input("How old are you? "))

#   # Informs the user to input a number if a non-number string was input
#   except:
#     print("Please enter a number.")

#   else:
#     break


while (True):
  options = ["swimming", "dancing", "tennis"]
  answer = input("What is your favorite sport?\nSwimming\nDancing\nTennis\n").lower()

  # if (answer != "yes" and answer != "no"):
  #   print("Please enter yes or no.")
  
  # else:
  #   break

  if answer.lower() in options:
    break