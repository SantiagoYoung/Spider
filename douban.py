#__author__: viber
#_*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup
import re
import time

header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
urls = [ 'https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25) ]
movies = []

def parse_one_movie(cursor, infos):
    url = infos.find("a", href=re.compile(r"https://movie\.douban\.com/subject/[0-9]+/"))["href"]
    titles = infos.findAll("span", class_="title")
    title=""
    if isinstance(titles, list):
        for item in titles:
            title = title + item.get_text()
    else:
        title = titles.get_text()
    other_title = infos.find("span",class_="other").string[3:]
    rating_num = infos.find("span", class_="rating_num").string
    movie_info = infos.find("div", class_="bd").p.get_text().strip()
    movie_infos = movie_info.split("\n")
    director_actor = movie_infos[0].strip()
    other_infos = movie_infos[1].strip().split("/")
    if len(other_infos) == 3:
        year = other_infos[0].strip()
        region = other_infos[1].strip()
        movie_type = other_infos[2].strip()
    else:
        year = other_infos[0].strip() + "," + other_infos[1].strip() + "," + other_infos[2].strip()+other_infos[3].strip()
        region = other_infos[4].strip()
        movie_type = other_infos[5].strip()
    introduce = infos.find("span", class_="inq")
    if introduce != None:
        introduce = introduce.string
    else:
        introduce = ""
    movie = [title,\
            other_title,\
            url,\
            rating_num,\
            director_actor,\
            year,\
            region,\
            movie_type,\
            introduce]
    movies.append(tuple(movie))

def get_url_info(cursor, url):
    url_info = requests.get(url, header)
    content = url_info.content.decode("utf-8")
    soup = BeautifulSoup(content, "lxml")
    items = soup.findAll("div", class_="item")
    for item in items:
        parse_one_movie(cursor, item)
    time.sleep(1)

for url in urls:
    get_url_info(1, url)

print(movies)
