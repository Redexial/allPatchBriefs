from urllib import request
from django.shortcuts import render
from django.template import loader
from bs4 import BeautifulSoup
import requests
import lxml

# Create your views here.

def index(req):
    contents = []
    file = open(".\\briefs\\templates\\briefs\\index.html", "r")
    dab = file.read() 
    newSoup = BeautifulSoup(dab,"lxml")
    for i in range(10,13):
        for j in range(1,26):
            r=requests.get("https://www.leagueoflegends.com/es-es/news/game-updates/patch-%u-%u-notes/"%(i,j))
            if(r.status_code == 200):
                print(r)
                soup = BeautifulSoup(r.content,"lxml")
                try:
                    xyalpha = soup.find(id="patch-patch-highlights").find_parent().find_next_sibling().find_next().find_next().find_next().find_next()
                except BaseException as e:
                    print(e)
                    continue
                contents.append(xyalpha)
                newSoup.append(xyalpha)
        with open(".\\briefs\\templates\\briefs\\index.html", "wb") as file:
            file.write(newSoup.prettify("utf-8"))
    return render(req, "briefs/index.html")