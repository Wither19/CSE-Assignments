# 1. Initialize list of names
names = ["John", "Matt", "Sophia", "Jeff", "Angela", "Dee"]

# 2. Display list size and content
print(f"The list has {len(names)} elements, and the the elements are {names}")

# 3. Add three new names to the list
names.append("Helen")
names.append("Mike")
names.append("Sam")

# 4. The same list display message, with the new names added
print(f"After adding the names Helen, Mike and Sam, the list has {len(names)} elements, and the the elements are {names}")

# 5. Insert "Nico" into position 7 (index 6)
names.insert(6, "Nico")

# 6. Display the list again, with Nico
print(f"After adding Nico, the list has {len(names)} elements, and the the elements are {names}")

# 7. Ask the user for their math teacher and best friend's names and adding both to their proper place
math_teacher = input("What is your math teacher's name? ")
friend = input("What is your best friend's name? ")

names.insert(4, math_teacher)
names.insert(7, friend)

# 8. Display the list again
print(f"After adding my math teacher and best friend's name, the list has {len(names)} elements, and the the elements are {names}")

# 9. Display the list in reverse
rev = names.copy()
rev.reverse()

print(f"My reversed list looks like this: {rev}")

# 10. Add "Jeff"
names.append("Jeff")

# 11. Get a count of how many times "Jeff" appears in the list
print(f"This is how many times the name Jeff is in my list: {names.count('Jeff')}")

# 12. Remove the 5th element from the list and display the list again
names.pop(5)
print(f"After removing the 5th element, the list has {len(names)} elements, and the the elements are {names}")

# 13. Remove the last, then 4th element and display the result
print(f"After removing the last and 4th elements, the list has {len(names)} elements, and the the elements are {names}")

# 14. Display certain results based on names in the list
if "Sam" in names or "Jeff" in names:
  print("I also know two people with the same name.")

if "Helen" in names:
  print("This is my favorite name.")

if "Joshua" not in names:
  print("It's sad you don't know Joshua.")
elif "Joshua" in names:
  print("Wow, that's my son's name!")

# 15. Print the final sorted list
names.sort()
print(f"Here is my sorted list: {names}")