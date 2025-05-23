import time

menu_items = ["Cheeseburger", "Hamburger", "Quarter Pounder", "Big Mac"]
menu_prices = [5.59, 1.79, 5.89, 5.59]

sizes = ["Small", "Medium", "Large"]

fry_prices = [1.00, 2.00, 2.99]

drinks = ["Sprite", "Coke", "Lemonade"]
drink_prices = [2.39, 2.39, 2.49]

packet_prices = [0.25, 0.30]

bought_items = []

# Made order and order_prices a combined 2D list.
order = [[], []]

combo = ["burger", "fries", "drink"]

discount = 0

subtotal = 0.00

# Function to get a user's yes-or-no response. yes or y returns true, no or n returns false
def y_or_n(response):
  if (response.lower() == "yes" or response.lower() == "y"):
    return True

  else:
    return False

# Prints an array of menu items with their associated prices, with changeable spacing.
def menu_print(items, prices, spacing=20):
  n = 0

  for item in items:
    price = prices[n]

    print(f"{item:{spacing}}${price:.2f}")

    n += 1

  n = 0

# Gets the price of the choice based on the index of that choice.
def get_price(choice, prices, arr):
  price = prices[arr.index(choice)]
  return price


# Used for ketchup / honey mustard when the user needs to input a quantity of something they want.
def ask_for_number(name):
  prompt = input(f"How many {name} would you like? ")
  prompt = int(prompt)

  return prompt

def add_to_order(generic, name, price):
  if (generic != ""):
    bought_items.append(generic)

  order[0].append(name)
  order[1].append(price)

# Prints information about the item you just added to the order.
def item_info_print(item, size=""):
  if (size != ""):
    print(f"You chose {size} {item}. Your subtotal is now ${subtotal:.2f}")
  else:
    print(f"You chose a {item}. Your subtotal is now ${subtotal:.2f}")


print("Welcome to McDonald's\nWhich hamburger would you like?\n")

menu_print(menu_items, menu_prices)


chosen_burger = input("\nEnter the burger name: ").capitalize()

# if (chosen_burger in menu_items):
if (chosen_burger in menu_items):
  price = get_price(chosen_burger, menu_prices, menu_items)

  subtotal += price
  add_to_order("burger", chosen_burger, price)

  item_info_print(chosen_burger)
  time.sleep(1.25)

else:
  print("You need to choose a burger on the menu.")

fries = input("Would you like fries (yes / no)? ")

chosen_fries = ""

if y_or_n(fries):
  print("What size would you like?\n")

  menu_print(sizes, fry_prices, 8)

  chosen_fries = input("\nEnter size: ").capitalize()

  if (chosen_fries in sizes):

    if (chosen_fries == "Small" or chosen_fries == "Medium"):

      mega = input("Would you like to mega-size (yes / no)? ")

      if y_or_n(mega):
        chosen_fries = "Large"
    price = get_price(chosen_fries, fry_prices, sizes)

    subtotal += price
    add_to_order("fries", f"{chosen_fries} fries", price)

    item_info_print(chosen_fries)
    time.sleep(1.25)

  else:
    print("You need to choose a size of fries.")

drink = input("Would you like a drink (yes / no)? ")

if y_or_n(drink):
  print("What drink would you like?\n")

  menu_print(drinks, drink_prices, 10)

  chosen_drink = input("\nEnter drink: ").capitalize()

  drink_price = get_price(chosen_drink, drink_prices, drinks)

  if (chosen_drink in drinks):

    print("\nWhat size? ")

    n = 0

    for size in sizes:
      print(size)

      n += 1

    chosen_drink_size = input("Enter size: ").capitalize()

  else:
    print("You need to choose a drink on the menu.")

  if (chosen_drink_size == "Small"):
    drink_price -= 0.50

  elif (chosen_drink_size == "Large"):
    drink_price += 0.50

  subtotal += drink_price

  formatted_drink = f"{chosen_drink_size} {chosen_drink}"

  add_to_order("drink", formatted_drink, drink_price)

  item_info_print(chosen_drink, chosen_drink_size)
  time.sleep(1.25)

  ketchup_amount = ""
  honey_mustard_amount = ""

  ketchup = input(f"Would you like to add ketchup for ${packet_prices[0]:.2f} / packet (yes / no)? ")

  if y_or_n(ketchup):
    ketchup_amount = ask_for_number("packets of ketchup")

    subtotal += packet_prices[0] * ketchup_amount
    add_to_order("", f"{ketchup_amount} Ketchup packet(s)", packet_prices[0] * ketchup_amount)

    item_info_print("ketchup packet(s)", ketchup_amount)
    time.sleep(1.25)

  honey_mustard = input(f"Would you like to add honey mustard for ${packet_prices[1]:.2f} a packet (yes / no)? ")

  if y_or_n(honey_mustard):
    honey_mustard_amount = ask_for_number("packets of honey mustard")

    subtotal += packet_prices[1] * honey_mustard_amount
    add_to_order("", f"{honey_mustard_amount} Honey mustard packet(s)", packet_prices[1] * honey_mustard_amount)

    item_info_print("honey mustard packet(s)", honey_mustard_amount)
    time.sleep(1.25)

  else:
    print(f"No honey mustard. Your subtotal is now ${subtotal:.2f}.")

print("Here is your order:\n")

menu_print(order[0], order[1], 30)

order_matches_combo = bought_items == combo

if (order_matches_combo):
  subtotal -= 1
  discount_display = "Discount:"
  print(f"\n{discount_display:30}($1.00)")

subtotal_display = "Subtotal:"
sales_tax_display = "Sales Tax:"
total_display = "Your Total:"


print(f"{subtotal_display:30}${subtotal:.2f}")

sales_tax = 6
sales_tax_amount = subtotal / (100 / 6)
total = subtotal + sales_tax_amount
nothing = ""

print(f"\n{sales_tax_display:} ({sales_tax}%):{nothing:14}${sales_tax_amount:.2f}")

print(f"\n{total_display:30}${total:.2f}")