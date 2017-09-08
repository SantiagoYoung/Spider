#!/bin/python3
import requests
from datetime import datetime
from bs4 import BeautifulSoup

item = 0
movies = []
begin = datetime.now()
for i in range(10):
    url = "http://movie.douban.com/top250?start=%s&filter=" % item
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    body = soup.body
    all_movies = body.find_all("ol", class_="grid_view")
    for _movie in all_movies:
       detail =  _movie.find_all("div", class_="hd")
    for _name in detail:
        movies.append(_name.find("span",class_="title").string)
end = datetime.now()
for i in movies:
    print(i)
    print("\n")

print(len(movies))
print( (end - begin).seconds)
print(movies[0])
