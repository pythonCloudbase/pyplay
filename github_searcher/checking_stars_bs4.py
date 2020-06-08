# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# websitecode = urlopen("https://github.com/fanbyprinciple").read().decode('utf8')
# soup=BeautifulSoup(websitecode, "html.parser")
# links=soup.findAll("a")
# print(links)

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.columbia.edu/~fdc/utf8/"
r = requests.get(url)

encodedText = r.text
soup = BeautifulSoup(encodedText)

print(soup.prettify("utf-8"))
