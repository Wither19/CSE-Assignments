"""
# Step 1

song = 2 + 1 
song = 3.0 
song = "geese" 
print(song)

# Step 3

mystery_value = type("Hello World!")
print(mystery_value)

# Step 4

a = 1.8
b = "King Henry VIII"
c = False
d = 5

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# Step 6

print(type("1")) 
print(type(-10)) 
print(type(False)) 
print(type("False")) 
print(type(3.14))
# Step 8
x = input("What is your name? ") 
y = input("What is your age? ")

print("Hello ", x)
print("You are", y, "years old")

# Step 11

first_age = input("What is the age of person 1? ")
second_age = input("What is the age of person 2?  ")

difference = first_age - second_age

print("Person 1 is", difference, "years older than person 2.")

# Step 12

first_age = input("What is the age of person 1? ")
second_age = input("What is the age of person 2?  ")

difference = int(first_age) - int(second_age)

print("Person 1 is", difference, "years older than person 2.")
# Step 13

print(int(3.14159))
print(str(8675309))
print(bool(0))
print(bool(1))
print(float(10))

# Step 18

studs_in_class1 = 27
studs_in_class2 = 31
studs_in_class3 = 13
sum_of_students = studs_in_class1 + studs_in_class2 + studs_in_class3

average_student_count = int(sum_of_students / 3)
print(average_student_count)


# Step 19

print(type(input("type in a name: "))) 
print(type(input("type in a number: "))) 
print(type(input("Enter anything: ")))


# Step 20

x = input("pick a number:")

if (int(x) < 10): 
  print("too low")
else: 
  print("too high")

# Step 22

print(False) 
print(5==4) 
print(2+6==5) 
print(5!=5) 
print(5<4) 
print(4>=5)

# Step 25

# and operator 
sleep = 7         #Modify this number to see how it changes the output 
breakfast = True  #Modify this number to see how it changes the output 
print (sleep>=8 and breakfast==True) 

# or operator 
food = "cake"     #Modify this food to see how it changes the output 
print(food=="cake" or food=="muffins") 

# not operator 
movie = "like"    #Modify this to say "dislike" to see how it changes the output 
print (movie!="like")

# Step 29

guesses = 0  # Change this number to see how the code output changes. 

if guesses >= 1: 
  x = int(input("pick a number:")) 
  if x < 10: 
    print("too low") 
  else: 
    print("too high") 
else: 
  print("You have run out of guesses!")
"""

# Variable and conditional program

x = 17
y = input("Guess the number:")
y = int(y)

if (y > x):
    print("Too high, try again")
elif (y < x):
    print("Too low, try again")
else:
    print("You guessed the number!")