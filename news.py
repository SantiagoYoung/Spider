#__author__: viber
#__version__: 1.0

import requests
from bs4 import BeautifulSoup
from lxml import etree
r = requests.get("http://news.163.com/rank/")
#body = BeautifulSoup(r.content, "lxml").body
html = etree.HTML(r.content)
result = html.xpath("//div[@class='area-half left']//tr/td[@class='red' or @class='gray']")
reply = html.xpath("//div[@class='area-half right']//tr/td[@class='red' or @class='gray']")
print(len(result))
print(len(reply))

trtr = html.xpath("//div[@class='area-half right']//tr")
print(trtr[1].findall("*")[1].text)
print(trtr[0].find(".//td"))
print(trtr[1].find(".//td[@class='red']//span").text)
