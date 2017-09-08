#__author__ : Viber
#_*- coding: utf-8 -*_

import requests
import re
from bs4 import BeautifulSoup

r = requests.get("https://movie.douban.com/top250")
soup = BeautifulSoup(r.content, "lxml")
body = soup.body
items = body.find_all("div", class_="item")

item1 = items[0]
href = item1.find("a", href=re.compile("https://movie\.douban\.com/subject/[0-9]+/"))["href"]
director = items[0].find("div", class_="bd").p.get_text().strip().split("\n")[0].strip()
title = ""
titles = items[0].find_all("span", class_="title")

for t in titles:
    title = t.string + " "
others = items[0].find_all("span", class_="other")
for o in others:
    title = title + o.string + " "
ranking = items[0].find("span", class_="rating_num").string
intro = items[0].find("span", class_="inq").string
detail = items[0].find("div", class_="bd").p.get_text().strip().split("\n")[1].strip().split("/")
year = detail[0]
country = detail[1]
category = detail[2]
new_title = ""
for i in title.strip().split("/"):
     new_title += i.strip()

print(href, title, ranking, intro, year, country, category)

print(tuple([href, title, ranking, intro, year, country, category]))
print(category)

