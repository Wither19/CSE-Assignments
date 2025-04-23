my_list = ["oranges", "apples", "bananas", "melon", "grapes"]


# While loop version (Update lists with this)

# index = 0
# while (index < len(my_list)):
#   if my_list[index] == "bananas":
#     my_list[index] = "pineapples"
#   print("Favorite fruit:", my_list[index])
#   index += 1

# print("end")


# For loop version (use just for a readonly item)

for item in my_list:
  if item == "bananas":
    item = "pineapples"
  print("Favorite fruit:", item)

print("My list has the following items:", my_list)