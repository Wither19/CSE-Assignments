import sys 
#*********************Function declarations***********************************


# You should declare your inputChoice here
""""This Function validates that the user only entered on of the options
and it will continue asking the user to re-enter until they type in one of the options"""

def inputChoice(message, options, error="Invalid option. Please try again."):
  answer = ""
  response_list = ""

  for o in options:
    response_list += f"\n{o}"

  while (answer not in options):
    answer = input(message + " ").lower()

    if (answer not in options):
      print(error)
    
  return answer


# You should declare your inputNumber here
""""This Function validates that the user only entered number
and it will continue asking the user to re-enter until they type in a numebr"""
def inputNumber(message):
    number = 0
    

    while (True):
      try:
        response = input(message)
        number = int(response)

      except:
        print("Please type in a number")

      else:
        break

    return number


# You should declare the isAuthenticated function here
""""This Function validates that the user pin number matches 3487. 
    It will allow the user to try 3 times. If correct then you will 
    return a True and if incorrect you will return a False."""
def isAuthenticated(pin):
    validated = False
    attempt = 1

    while (not validated):

      # If the pin is guessed correctly
      if (pin == 3487):
         
         print("Correct PIN #.\n")
         validated = True

         break
      
      # If the user cannot guess the pin on the third try
      elif (attempt == 3):
         print("You have reached the maximum number of attempts. Please wait 24 hours before trying again. Thank you, and have a blessed day!")
         sys.exit()
      
      # Any other incorrect guess
      else:
            
        print("Incorrect PIN #\n")

        if (attempt == 2):
          print(f"You have 1 attempt left.")
        
        else:
          print(f"You have {3 - attempt} attempts left.")

        pin = inputNumber("Please enter your pin #. ")

      attempt += 1

    return validated



#*************************Main Program*****************************************

print("Welcome to MyCCA Bank ATM".center(50))

# Part I Authentication Screen.
pin = inputNumber("Please enter your pin #. ")

if isAuthenticated(pin)==True: # In tis line of code you are callthe function isAuthenticate(pin)
    
  
  option = ""
  while (option != "4"):

      #Part II
      #Display here the Main menu with the correct format

      # 2D List containing the option numbers in the first list, and the option names in the second.
      menu_options = [["1", "2", "3", "4"], ["Withdraw", "Deposit", "Check Balance", "Return Card"]]

      for option in menu_options[0]:
        print(f"{option}{".":5} {menu_options[1][int(option) - 1]}")

      option = inputChoice("Please select option:", menu_options[0]) #You can delete this line once you add the correct code

      


      # Add conditionals to execute the code for the different options.
      #Part III Withdraw
      #1.	Withdraw



      #Part IV Deposit
      #2.	Deposit



      #Part V Check Balance
      #3.	Check Balance



      #Part IV ExitReturn Card
      #4.	Check Balance





  #Part VI Return Card
  #Once the while breaks display the message that option 4 should display
