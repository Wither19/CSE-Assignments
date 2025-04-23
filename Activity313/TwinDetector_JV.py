# The special color and number values that trigger unique responses.
fav_color = "red"
fav_number = 7
sister_fav_color = "yellow"
close_fav_number = 8

# The inputs for favorite color / number.
color_prompt = input("What is your favorite color? ")
number_prompt = input("What is your favorite number? ")

# Conditional to decide what to print based upon user input.
if (color_prompt == "red" and int(number_prompt) == 7):
    print("Hey! You are just like me. We are twins!")
elif (color_prompt == "yellow"):
    print("That is my sister’s favorite color.")
elif (int(number_prompt) == 8):
    print("You were so close to my favorite number.")
else:
    print("Your favorite color is: {} and your favorite number is {}. You seem to be unique.".format(color_prompt, number_prompt))