import colorama as color

print(f'{"Survey":^50}')
print(f'{"Welcome to My Survey":^50}')
name = input("Please enter your name: ")

# Introduction to Survey
print(f'\nWelcome to my survey, {name}.')
print()
print(f'{"You will be presented with 5 questions. Each question has 2 possible answers.":<50}')
print(color.Fore.YELLOW + f'{"Note: You can only pick an answer from the list.":<30}')
print(color.Fore.WHITE)

input("Press enter to continue...\n")

def question(q, responses, err_msg="Not a correct response."):
  response_list = ""

  for r in responses:
    response_list += f"{r.capitalize()}\n"

  response_list += "Answer: "

  answer = ""

  while (answer not in responses):
    print(color.Fore.YELLOW + q + color.Fore.WHITE)

    answer = input(response_list).lower()

    if (answer not in responses):
      print(err_msg)
        
  return answer.capitalize()

# Questions
answer1 = question("Question 1: Never need sleep, or always need 10 hours of sleep?", ["no sleep", "10 hours"])

answer2 = question("Question 2: Dance solo in public or sing solo in public?", ["dance", "sing"])

answer3 = question("Question 3: Laugh like a hyena or a snort like a pig?", ["hyena", "snort"])

answer4 = question("Question 4: Big truck or sports car?", ["truck", "sports"])

answer5 = question("Question 5: Give up ice cream or pizza for the rest of your life?", ["pizza", "ice cream"])

# Display Results
print("\nEnd of Survey.\n")
print(f"""Survey Results:
                Q1: Never need sleep, or always need 10 hours of sleep? {answer1}
                Q2: Dance solo in public or sing solo in public? {answer2}
                Q3: Laugh like a hyena or a snort like a pig? {answer3}
                Q4: Big truck or sports car? {answer4}
                Q5: Give up ice cream or pizza for the rest of your life? {answer5}""")

print("Thank you for your time.\nHave a blessed day!\n")














