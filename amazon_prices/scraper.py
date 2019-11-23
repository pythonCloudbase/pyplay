import requests 
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Wacom-CTL-472-6-inch-3-5-inch-Graphic/dp/B078HRR1XV/ref=sr_1_3?keywords=Wacom+1+472&qid=1574496026&s=computers&sr=1-3'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").getText().strip()
    price = soup.find(id="priceblock_ourprice").getText().strip()[2:9]
    without_comma = price.split(",")
    fprice = float( "".join(without_comma))
    print(title, " : ", fprice)

check_price()

