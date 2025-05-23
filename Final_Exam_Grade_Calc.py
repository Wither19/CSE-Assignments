print("Python Final Exam Grade Calculator\n")

current_grade = input("What is your current grade for a class? (%) ")
current_grade_factor = 0

try:
  current_grade = float(current_grade)

except:
  print("Please enter a valid number.")

else:
  current_grade_factor = current_grade * 0.85

exam_grade = input("What is your desired grade for the exam in that class? (%) ")
exam_grade_factor = 0

exam_weight = 0.15

try:
  exam_grade = float(exam_grade)

except:
  print("Please enter a valid number.")

else:
  exam_grade_factor = exam_grade * exam_weight


resulting_grade = current_grade_factor + exam_grade_factor

print(f"Final Grade: {resulting_grade:.2f}%")

needed_grade = (89.5 - current_grade * (1 - exam_weight)) / exam_weight

print(f"Needed Grade to get an A: {needed_grade:.2f}%")