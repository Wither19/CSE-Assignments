print("Python Final Exam Grade Calculator\n")

current_grade = input("What is your current grade for a class? (%) ")

try:
  current_grade = float(current_grade)

except:
  print("Please enter a valid number.")

exam_grade = input("What is your desired grade for the exam in that class? (%) ")

try:
  exam_grade = float(exam_grade)

except:
  print("Please enter a valid number.")


resulting_grade = (current_grade * 0.85) + (exam_grade * 0.15)

print(f"Final Grade: {resulting_grade:.2f}%")