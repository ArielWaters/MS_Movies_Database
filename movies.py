import random
import movie_storage


def list_movies():
    """Provides a list of the movies in the database"""

    movies_data = movie_storage.list_movies()
    movies = []
    for name, movie in movies_data.items():
        movies.append({'name': name, 'rating': movie['rating'], 'year': movie['year']})

    print(len(movies), "movies in total")
    for index, movie in enumerate(movies):
        print(f"{index + 1}. {movie['name']}: {movie['rating']}, {movie['year']}")


def add_movie():
    """Adds a new movie to the list of movies in the database"""

    name = input("Enter new movie name: ")

    movie_storage.add_movie(name)


def del_movie():
    """Deletes a selected movie from the list of movies in the database"""

    name = input("Enter movie name to delete: ")

    movie_storage.delete_movie(name)

    print(f"Movie {name} successfully deleted!")


def update_movie():
    """Updates the information of a selected movie in the list of movies in the database"""

    name = input("Enter movie name: ")
    rating = input("Enter new movie rating (0-10): ")

    movie_storage.update_movie(name, rating)

    print(f"Movie {name} successfully updated!")


def stats():
    """Calculates and displays statistics for the movies in the database"""

    movies_data = movie_storage.list_movies()
    ratings = [float(movie['rating']) for movie in movies_data.values()]

    # Average rating
    avg_rating = sum(ratings) / len(ratings)
    print(f"Average rating: {avg_rating:.2f}")

    # Median rating
    n = len(ratings)
    sorted_ratings = sorted(ratings)
    if n % 2 == 0:
        median_rating = (sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2
    else:
        median_rating = sorted_ratings[n // 2]
    print(f"Median rating: {median_rating:.2f}")

    # Best movie
    best_movies = [name for name, movie in movies_data.items() if movie['rating'] == max(ratings)]
    for movie in best_movies:
        print(f"Best movie: {movie}, {max(ratings)}")

    # Worst movie
    worst_movies = [name for name, movie in movies_data.items() if movie['rating'] == min(ratings)]
    for movie in worst_movies:
        print(f"Worst movie: {movie}, {min(ratings)}")


def random_movie():
    """Selects a random movie from the list and prints its name and rating"""

    movies_data = movie_storage.list_movies()
    movie_name = random.choice(list(movies_data.keys()))
    movie = movies_data[movie_name]
    print(f"Your movie for tonight: {movie_name}. It's rated {movie['rating']}.")


def search_movie():
    """Searches for movies based on a partial name entered by the user"""

    user_input = input("Enter part of movie name: ").lower()
    movies_data = movie_storage.list_movies()
    found_movies = []
    for name, movie in movies_data.items():
        if user_input in name.lower():
            found_movies.append(f"{name}, {movie['rating']}")
    if found_movies:
        print("\n".join(found_movies))
    else:
        print("No movies found")


def sorted_movies():
    """Sorts and displays the movies in descending order of their ratings"""

    movies_data = movie_storage.list_movies()
    sorted_movies_data = sorted(movies_data.items(), key=lambda x: float(x[1]['rating']), reverse=True)

    for name, movie in sorted_movies_data:
        print(f"{name}, {movie['rating']}")


def main():
    while True:
        print("******** My Movies Database ********")
        print("Menu:")

        menu_movies = {
            "0.": "Exit",
            "1.": "List movies",
            "2.": "Add movie",
            "3.": "Delete movie",
            "4.": "Update movie",
            "5.": "Stats",
            "6.": "Random movie",
            "7.": "Search movie",
            "8.": "Movies sorted by rating",
            "9.": "Generate website"
        }

        for key, value in menu_movies.items():
            print(key, value)

        print()
        user_input = int(input("Enter choice (0-8): "))
        if user_input == 0:
            print("Bye!")
            break
        elif user_input == 1:
            list_movies()
            print()
        elif user_input == 2:
            add_movie()
            print()
        elif user_input == 3:
            del_movie()
            print()
        elif user_input == 4:
            update_movie()
            print()
        elif user_input == 5:
            stats()
            print()
        elif user_input == 6:
            random_movie()
            print()
        elif user_input == 7:
            search_movie()
            print()
        elif user_input == 8:
            sorted_movies()
            print()
        elif user_input == 9:
            movie_storage.generate_website()
            print()

        ending = input("Press enter to continue")


if __name__ == "__main__":
    main()
