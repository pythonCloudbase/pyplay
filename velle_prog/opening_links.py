import requests, sys, webbrowser, bs4
print('Searching ...')
res = requests.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.findAll('a')

for i in linkElems:
    print(i.parent)


###http://automatetheboringstuff.com/2e/chapter12/