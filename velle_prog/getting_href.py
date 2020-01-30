import bs4 as bs
import urllib.request
import re

html_page = urllib.request.urlopen("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=china+cyber&btnG=")
soup = bs.BeautifulSoup(html_page)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print(link.get('href'))