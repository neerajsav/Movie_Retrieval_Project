import requests

def get_movie_info(movie_title, api_key):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data["Response"] == "True":
            title = data["Title"]
            year = data["Year"]
            genre = data["Genre"]
            director = data["Director"]
            plot = data["Plot"]

            print("Movie Information:")
            print(f"Title: {title}")
            print(f"Year: {year}")
            print(f"Genre: {genre}")
            print(f"Director: {director}")
            print(f"Plot: {plot}")

        else:
            print("Movie not found.")
    else:
        print("Request failed. Check your network connection.")

# User input for movie title and API key
movie_title = input("Enter the movie title: ")
api_key = "f55091d5"

# Call the function to retrieve movie information
get_movie_info(movie_title, api_key)
