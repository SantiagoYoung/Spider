#!/bin/python3
import requests
from bs4 import BeautifulSoup




if __name__ == "__main__":
    url = [
            "http://music.163.com/#/discover/artist"
          ]
    r = requests.get(url[0])
    bs = BeautifulSoup(r.content.decode(), "html.parser")
    body = bs.body
    artists = body.find_all("ul", attrs={"class":"m-cvrlst mcvrlst-5 f-cb"})
#    singers = bs.find_all("div ul", class_ = "m-cvrlst m-cvrlst-5 f-cb") 
#    singer_div = bs.find("div", class_ = "m-sgerlist")
#    singer_ul = bs.select("#m-artist-box")
    print(artists)
#    singer_ul = singer_div.contents()[0]
#    for singer in singers:
#        for singer_detail in singers.children:
#            singer_name = singer_detail.select("li > p")[0]
#            print(singer_name.text)


