# Present numbered list for the measurements
print("BMI Calculator\n\n1. Standard\n2. Metric")

measurements = input("Please enter measurement options: ")

measurements = int(measurements)

bmi = 0
cat = ""

# Decides whether to use customary or metric units based off of user input
if (measurements == 1):
  print("Please enter height: ")

  ft = input("Feet: ")
  inch = input("Inches: ")

  print("Please enter weight: ")

  lbs = input("Pounds: ")

  bmi = float(lbs) / (((float(ft) * 12) + float(inch)) ** 2) * 703

elif (measurements == 2):
  print("Please enter height: ")

  cm = input("Centimeters: ")

  print("Please enter weight: ")

  kg = input("Kilograms: ")

  bmi = float(kg) / ((float(cm) / 100) ** 2)

# Decides BMI category

if (bmi < 18.5):
  cat = "Underweight"

elif (bmi >= 18.5 and bmi < 25):
  cat = "Normal"

elif (bmi >= 25 and bmi < 30):
  cat = "Overweight"

elif (bmi > 30):
  cat = "Obese"


# Prints results to terminal
print("Your BMI is {}\n\n{}".format(str(round(bmi, 1)), cat))