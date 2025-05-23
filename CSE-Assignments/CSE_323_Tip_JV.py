# Calculates a tip amount based off of the total of the meal in dollars, and the tip percentage.
def calc_tip(total_meal, tip_percent):
  # total_meal = 25
  # tip_percent = 20 (%)


  tip_ratio = float(tip_percent) / 100
  
  return float(total_meal) * tip_ratio

valid_tips = ["15", "18", "20"]

while (True):
  total = input("Please enter the total of your meal: ")

  tip = input("Please enter the tip % (15%, 18%, 20%): ")

  if (tip not in valid_tips):
    print("Please enter a valid tip amount.")
    continue
  
  else:
    try:

      total = float(total)
      tip = int(tip)
    
    except:
      print("Either your total or tip isn't a number.")

    else:
      calculated_tip = calc_tip(total, tip)
      print(f"\nYour tip amount is: ${calculated_tip:.2f}")
      print(f"Your total including the tip is: ${(total + calculated_tip):.2f}")
      break