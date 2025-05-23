# Gets the user's weight in pounds and converts to a float
weight = input("Please enter your current weight (lbs.): ")
weight = float(weight)

print("I have information for the following planets:\n1. Venus\n2. Mars\n3. Jupiter\n4. Saturn\n5. Uranus\n6. Neptune")

# Asks the user which planet they are going to, using numbered values
planet = input("Which planet are you visiting? ")
planet = int(planet)

# Lists of planet names and weight conversions by planet
planet_names = ["Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
weight_conversions = [0.78, 0.39, 2.65, 1.17, 1.05, 1.23]

# Selects from both lists using the (0-based) index of the user response
if (planet > 0 and planet <= 6):
  chosen_planet = planet_names[planet - 1]
  planet_gravity = weight_conversions[planet - 1]

# Multiplies the weight by the gravity to get the resulting weight
  converted_weight = weight * planet_gravity

  print("Your weight would be {} pounds on {}.".format(str(converted_weight), chosen_planet))