# User input prompts for all needed info
speed_input = input("Do you know how fast you were going? ")
speed = int(speed_input)

# Function to convert the 'yes or no' string response to boolean value
def bday_bool(answer):
    if (answer == "yes" or answer == "y"):
        return True
    elif (answer == "no" or answer == "n"):
        return False

bday_input = input("Is today your birthday? ")
bday = bday_bool(bday_input)

# Speed thresholds for deciding ticket size, are increased by 5 if 'bday' is true

min_speed = 60
max_speed = 80

if bday:
    min_speed = min_speed + 5
    max_speed = max_speed + 5
    
if (speed <= min_speed):
    print("No ticket")
    
elif (speed > min_speed and speed <= max_speed):
    print("Small ticket")
    
elif (speed > max_speed):
    print("Big ticket")