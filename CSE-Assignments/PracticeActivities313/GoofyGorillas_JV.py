gorilla_one = input("Is Gorilla One smiling? ")
gorilla_two = input("Is Gorilla Two smiling? ")

# Change both responses to lowercase just in case
gorilla_one = gorilla_one.lower()
gorilla_two = gorilla_two.lower()

# Both gorillas are content
if (gorilla_one == "yes" and gorilla_two == "yes"):
    print("Everything is ok")
    
# Any other case (one, or both are mad)    
elif ((gorilla_one == "no" and gorilla_two == "yes") or (gorilla_one == "yes" and gorilla_two == "no") or (gorilla_one == "no" and gorilla_two == "no")):
    print("Alert: trouble with the gorillas")
else:
    print("Yes or no?")