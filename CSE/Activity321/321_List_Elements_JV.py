string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

# Function to inform the user about the list, the amount of elements, and the elements in it.
def print_list_info(my_list, list_name):

  print(f'{list_name} has {len(my_list)} elements. This is the list {my_list}')

# Check whether the input item is in 'food'.
def is_in_food(item):
  if (item in food):
    print(f"One {item}, coming up!")
  else:
    print(f"Sorry, we don't carry {item}s")

print_list_info(string_list, "string_list")
print_list_info(int_list, "int_list")
print_list_info(float_list, "float_list")
print_list_info(boolean_list, "boolean_list")
print_list_info(mixed_list, "mixed_list")
print_list_info(empty, "empty")

# a list of menu items
food = ["Burger", "Shake", "Fries"]
first_menu_item = food[0]

print(first_menu_item, "is located at index 0.")
print("The second element of the list is", food[1])
print("The third element of the list is", food[2])
# "List index out of range"
# print(food[3], "is located at index 3")

# Negative indices start at the end
print(food[-1], "is located at index -1")

is_in_food("Burger")
is_in_food("Shake")
is_in_food("Fries")

# Check if pizza isn't in 'food', which should be True.
print(pizza not in food)



customer_order = ["Fries", "Shake"] # The preset customer order
item = input("What else would you like to order? ") # Seeing what you would like to add to the order
customer_order.append(item) # Adds the user input to the customer order

print("You ordered", customer_order) # Repeats to the user their full order.
answer = input("Is your order correct? ") # Asks if their full order is right.

if (answer == "yes"):
    print("Great! Your order is coming right up!")  # A yes response doesn't change the order list.
else:
    print("Okay, I will remove", item, "from your order.")
    customer_order.remove(item) # Removes the user input item to the order.

print("Your new order is", customer_order) # Prints the full order after the opportunity to remove an item is given.
