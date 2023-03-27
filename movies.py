import random

def list_movies(dictionary):
  print(len(dictionary), "movies in total")
  for key, value in dictionary.items(): 
    print(key, ":", value)

def add_movie(dictionary): 
  user_input1 = input("Enter new movie name: ")
  user_input2 = float(input("Enter new movie rating (0-10): "))
  dictionary[user_input1] = user_input2
  print(f"Movie {user_input1} successfully added")

def del_movie(dictionary): 
  user_input = input("Enter movie name to delete: ")
  if user_input not in dictionary: 
    print(f"Movie {user_input} doesn't exist!")
  elif user_input in dictionary: 
    del dictionary[user_input]
    print(f"Movie {user_input} successfully deleted!")
  
def update_movie(dictionary): 
  user_input1 = input("Enter movie name: ")
  if user_input1 not in dictionary: 
    print(f"Movie {user_input1} doesn't exist!")
  elif user_input1 in dictionary: 
    user_input2 = float(input("Enter new movie rating(0-10): "))
    dictionary[user_input1] = user_input2
    print(f"Movie {user_input1} successfully updated!")

def stats(dictionary): 
  ratings = list(dictionary.values())
  
  #average rating
  avg_rating = sum(ratings) / len(ratings)
  print(f"Average rating: {avg_rating:.2f}")

  #median rating
  n = len(ratings)
  sorted_ratings = sorted(ratings)
  if n % 2 == 0:
    median_rating = (sorted_ratings[n//2 - 1] + sorted_ratings[n//2]) / 2
  else:
    median_rating = sorted_ratings[n//2]
  print(f"Median rating: {median_rating:.2f}")
  
  #best movie
  best_movie = [title for title, rating in dictionary.items() if rating == max(ratings)]
  for movie in best_movie: 
    print(f"Best movie: {movie}, {dictionary[movie]}")
  
  #worst movie
  worst_movie = [title for title, rating in dictionary.items() if rating == min(ratings)]
  for movie in worst_movie: 
    print(f"Worst movie: {movie}, {dictionary[movie]}")

def random_movie(dictionary): 
  key, value = random.choice(list(dictionary.items()))
  print(f"Your movie for tonight: {key}. It's rated {value}.")

def search_movie(dictionary):
  user_input = input("Enter part of movie name: ")
  user_input = user_input.lower()
  for movie, rating in dictionary.items(): 
    if user_input in movie.lower(): 
      print(f"{movie}, {rating}")
  if user_input not in movie.lower(): 
    print("Movie not found")

def sorted_movies(dictionary): 
  sorted_dictionary = sorted(dictionary, key = dictionary.get, reverse = True)
  for item in sorted_dictionary: 
    print(item, dictionary[item])


def main():
  movies = {
      "The Shawshank Redemption": 9.5,
      "Pulp Fiction": 8.8,
      "The Room": 3.6,
      "The Godfather": 9.2,
      "The Godfather: Part II": 9.0,
      "The Dark Knight": 9.0,
      "12 Angry Men": 8.9,
      "Everything Everywhere All At Once": 8.9,
      "Forrest Gump": 8.8,
      "Star Wars: Episode V": 8.7
  }

  while True: 
    print("******** My Movies Database ********")
    print("Menu:")

    menu_dictionary = {
      "1.": "List movies",
      "2.": "Add movie",
      "3.": "Delete movie",
      "4.": "Update movie", 
      "5.": "Stats",
      "6.": "Random movie",
      "7.": "Search movie",
      "8.": "Movies sorted by rating"}
  
    for key, value in menu_dictionary.items(): 
      print(key, value)
  
    user_input = int(input("Enter choice (1-8): "))
    if user_input == 1:
      list_movies(movies)
    elif user_input == 2:
      add_movie(movies)
    elif user_input == 3:
      del_movie(movies)
    elif user_input == 4:
      update_movie(movies)
    elif user_input == 5: 
      stats(movies)
    elif user_input == 6:
      random_movie(movies)
    elif user_input == 7:
      search_movie(movies)
    elif user_input == 8: 
      sorted_movies(movies)
  
    ending = input("Press enter to continue")

if __name__ == "__main__":
  main()

