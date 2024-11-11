import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles.reverse()

with open("movies.txt", "w", encoding="utf8") as file:
    for title in titles:
        file.write(f"{title.getText()}\n")
