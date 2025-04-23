my_grades = [65, 90, 100]

total_grades = 0

for grade in my_grades:
  print("Grade:", grade)
  total_grades += grade

total_items = len(my_grades)

avg = total_grades / total_items

print("The avg. grade:", avg)