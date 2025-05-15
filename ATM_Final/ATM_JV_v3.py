import sys

# Validates that the input is part of a set of options, will loop continuously until a valid option is given
def inputChoice(message, options, error="Invalid option. Please try again."):
  answer = ""
  response_list = ""

  # The string to neatly display all options
  for option in options:
    response_list += f"\n{option}"

  while (answer not in options):
    answer = input(message + " ").lower()

    if (answer not in options):
      print(error)
    
  return answer

# Validates the input is a number
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


# Gives the user a number (attempts, that defaults to 3) of chances to input a specific PIN. Exits the program completely if the user runs out of attempts.
def isAuthenticated(pin, attempts=3):
    validated = False

    while (not validated):

      # If the pin is guessed correctly
      if (pin == 3487):
         
         print("Correct PIN #.\n")
         validated = True

         break
      
      # If the user cannot guess the pin on the third try
      elif (attempts == 3):
         print("You have reached the maximum number of attempts. Please wait 24 hours before trying again. Thank you, and have a blessed day!")
         sys.exit()
      
      # Any other incorrect guess
      else:
            
        print("Incorrect PIN #\n")

        if (attempts == 2):
          print(f"You have 1 attempt left.")
        
        else:
          print(f"You have {3 - attempts} attempts left.")

        pin = inputNumber("Please enter your pin #. ")

      attempts += 1

    return validated


def make_transaction(arr, transaction_type, amount):
  if (transaction_type == "withdraw"):
    amount *= -1

  arr[0].append(transaction_type)
  arr[1].append(amount)
  


#*************************Main Program*****************************************

print("Welcome to MyCCA Bank ATM")

# Part I Authentication Screen.
pin = inputNumber("Please enter your pin #. ")

if isAuthenticated(pin):
    
  # Initialize variables for the loop to change
  option = ""
  initial_balance = 5000.00

  # Transaction types, Transaction amounts (Withdrawal amounts are made negative in the function)
  transactions = [[], []]

  while (option != "4"):

      # 2D List containing the option numbers in the first list, and the option names in the second.
      menu_options = [["1", "2", "3", "4"], ["Withdraw", "Deposit", "Check Balance", "Return Card"]]

      for option in menu_options[0]:
        print(f"{option}{".":5} {menu_options[1][int(option) - 1]}")

      option = inputChoice("Please select option:", menu_options[0])

      # Be sure to check for a string "1", "2", "3" etc. in conditionals
      if (option == "1"):
        withdraw_amount = inputNumber("Please enter amount to withdraw ($): ")

        if (withdraw_amount > initial_balance):
          print("You have insufficient funds in your account to withdraw that amount.")
        
        else:
          # Handle adding the transaction to the list, and removing from the balance
          make_transaction(transactions, "withdraw", withdraw_amount)
          initial_balance -= withdraw_amount

          print("Transation has been completed successfully.")
          print(f"Amount withdrawn: ${withdraw_amount:.2f}".center(25))
          print(f"Current account balance: ${(initial_balance - withdraw_amount):.2f}".center(25))

        input("Press enter to return to the Main Menu ")

       



      #Part IV Deposit
      #2.	Deposit



      #Part V Check Balance
      #3.	Check Balance



      #Part IV Exit
      #4.	Exit





  #Part V Return Card
  #Once the while breaks display the message that option 4 should display
