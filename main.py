from bs4 import BeautifulSoup
import requests

connection = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
text_connection = connection.text

soup = BeautifulSoup(text_connection, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

print(all_movies)

# for i in all_movies:
#     papa = i.getText()
#     listofMovies.append(papa)

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

print(movies)
# print(listofMovies)
# print(*listofMovies)
#
# descending = listofMovies[::-1]
# print(descending)

with open("movies.txt", mode="w", encoding="utf-8") as my_file:
    for movi in movies:
        my_file.write(f"{movi}\n")



