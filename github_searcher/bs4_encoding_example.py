from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
# headers = {"User-Agent": USERAGENT}

url = "https://github.com/fanbyprinciple"

#resp = requests.get(url, headers=headers)
resp = requests.get(url)
http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(resp.content, 'lxml', from_encoding=encoding)

print(soup.prettify())