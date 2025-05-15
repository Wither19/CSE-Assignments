import sys

# Validates that the input is part of a set of options, will loop continuously until a valid option is given
def input_choice(message, options, error="Invalid option. Please try again."):
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
def input_number(message):
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
def is_authenticated(pin, attempts=3):
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

        pin = input_number("Please enter your pin #. ")

      attempts += 1

    return validated

# A centered print function
def centered_print(string, spacing=30):
  return print(string.center(spacing))

# Instead of typing an input to return to the menu every time
def go_to_menu():
  input("Press enter to return to the Main Menu ")

# The function that both handles deposits and withdrawals, but also displays the resulting changes to the balance
def make_transaction(arr, transaction_type, amount):
  print("Transation has been completed successfully.")

  # Makes the withdrawal amount negative to indicate the loss of money in the account.
  if (transaction_type == "withdraw"):
    amount *= -1
    print(f"Amount withdrawn: ${amount * -1:.2f}")

  elif (transaction_type == "deposit"):
    print(f"Amount deposited: ${amount:.2f}")

  print(f"Current account balance: ${(balance):.2f}")

  arr[0].append(transaction_type)
  arr[1].append(amount)


  


#*************************Main Program*****************************************

print("Welcome to MyCCA Bank ATM")

# Part I Authentication Screen.
pin = input_number("Please enter your pin #. ")

if is_authenticated(pin):
    
  # Initialize variables for the loop to change
  option = ""
  balance = 5000.00

  # Transaction types, Transaction amounts (Withdrawal amounts are made negative in the function)
  transactions = [[], []]

  while (option != "4"):

      # 2D List containing the option numbers in the first list, and the option names in the second.
      menu_options = [["1", "2", "3", "4"], ["Withdraw", "Deposit", "Check Balance", "Return Card"]]

      for option in menu_options[0]:
        print(f"{option}{".":5} {menu_options[1][int(option) - 1]}")

      option = input_choice("Please select option:", menu_options[0])

      # Be sure to check for a string "1", "2", "3" etc. in conditionals
      if (option == "1"):
        withdraw_amount = input_number("Please enter amount to withdraw ($): ")

        if (withdraw_amount > balance):
          print("You have insufficient funds in your account to withdraw that amount.")
        
        else:
          # Handle adding the transaction to the list, and removing from the balance
          withdraw_amount = float(withdraw_amount)
          balance -= withdraw_amount
          
          make_transaction(transactions, "withdraw", withdraw_amount)
          

        go_to_menu()

      elif (option == "2"):
        deposit_amount = input_number("Please enter amount to deposit ($): ")

        # No need to compare the deposit amount to another number
        deposit_amount = float(deposit_amount)

        balance += deposit_amount
        make_transaction(transactions, "deposit", deposit_amount)

        go_to_menu()

      elif (option == "3"):
        centered_print(f"ATM Account Balance: ${balance:.2f}")
        
        # Only attempts to print the list of transactions if the transaction lists contains something
        if (len(transactions[0]) != 0):
          centered_print("\n\nTransactions")

          print(f"{"Type":30}Amount\n")

          for transaction in transactions[0]:
            amount = transactions[1][transactions[0].index(transaction)]

            # Wrap negative numbers in parentheses
            if (amount < 0):
              amount = f"($ {amount:.2f})"

            else:
              amount = f"$ {amount:.2f}"

            print(f"{transaction.capitalize():25} {amount}")
          
        go_to_menu()

      # Return card and exit
      elif (option == "4"):
        print("Please wait while your card is returned...\n\nThank you for your business, and have a blessed day!")
        break