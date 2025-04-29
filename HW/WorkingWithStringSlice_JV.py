word = "Joseph"

# word[2] = "B" String characters cannot be directly reassigned

for i in range(0, len(word)):
  
  if (word[i].lower() == "n"): # Will only print if the current letter is n (My name doesn't have any n's)
    print(word[i]) # Prints new line after each character (by default)
  # print(word[i], end="-")

print("For loop:")

for letter in word:
  print(letter)


if "d" in word.lower():
  print("I found it")





other_word = "Calvary Chapel"

print(word[8:]) # Chapel
print(word[5:9]) # ry C


my_list = ["a", "b", "c", "d", "e", "f"]
my_string = "Hello world"

print(my_list[1:4]) # ["b", "c", "d"]
print(my_string[6:]) # "world"

# Step values
print(my_list[0:5:2]) # ["a", "c", "e"]
print(my_string[::2]) # "hlowrd"

print(my_list[-3:-1]) # ["d", "e"]
print(my_list[-5:]) # "world"

# Reversing a sequence
print(my_list[::-1]) # ["f", "e", "d", "c", "b", "a"]