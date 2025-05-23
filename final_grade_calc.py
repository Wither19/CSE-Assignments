print("Python Final Exam Grade Calculator\n")

current_grade = input("What is your current grade for a class? (%) ")
current_grade_factor = 0

exam_weight = 0.15

try:
  current_grade = float(current_grade)

except:
  print("Please enter a valid number.")

else:
  current_grade_factor = current_grade * 0.85

needed_grade = (89.5 - current_grade * (1 - exam_weight)) / exam_weight

print(f"Minimum Grade to get an A: {needed_grade:.2f}%")

if __name__ == "__main__":
  print(f"{needed_grade:.2f}")