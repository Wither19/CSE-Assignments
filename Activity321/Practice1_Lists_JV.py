movie_list = []

def display_list():
  if (len(movie_list) != 0):
    print("This is the current list:", movie_list)

  else:
    print("There are no movies in the list yet!")

def movies_not_blank():
  return len(movie_list) != 0

def is_valid_movie(movie):
  return movie != "" and movie not in movie_list

while (True):
  print("1. Add Favorite Movies (in order of preference)\n2. Remove a Favorite Movie\n3. Display 3 Favorite Movies (first, middle, last)\n4. Insert a Favorite Movie\n5. Display List of Favorite Movies\n6. Exit")
  option = input("Enter an option (1-6): ")

  if (option == "1"):

    movie_add = input("Enter the movie you would like to add: ")

    if (is_valid_movie(movie_add)):
      movie_list.append(movie_add)

      print(movie_add, "added!")

  elif (option == "2"):

    if (movies_not_blank()):
      display_list()

      movie_remove = input("Which movie would you like to remove? ")

      if (movie_remove in movie_list):
        movie_list.remove(movie_remove)

        print(movie_add, "removed!")

  elif (option == "3"):
    middle = round((len(movie_list) / 2) - 1)

    print(movies_not_blank())
    if (movies_not_blank()):
      print(f"Three of your favorite movies:\n{movie_list[0]}\n{movie_list[middle]}\n{movie_list[-1]}")

  elif (option == "4"):
    if (movies_not_blank()):
      display_list()
    movie_insert = input("What is the name of the movie? ")
    movie_insert_index = input("Where would you like to insert the new movie? ")
    movie_insert_index = int(movie_insert_index)

    if (is_valid_movie(movie_insert) and movie_insert_index < len(movie_list)):
      movie_list.insert(movie_insert_index - 1, movie_insert)
      print(movie_insert, "added at position", movie_insert_index)

  elif (option == "5"):
    display_list()

  elif (option == "6"):
    print("Have a nice day")
    break
  else:
    print("Invalid option, please try again.")