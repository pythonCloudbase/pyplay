import requests

url = "https://api.github.com/users/Sentdex/starred{/owner}{/repo}"
HEADERS = {'Authorization':'fanbyprinciple: d263fa634a5c13bce9eb7dea272d01e6573232ed '}
PARAMS = {'fanbyprinciple':  "d263fa634a5c13bce9eb7dea272d01e6573232ed" }
# headers={"content-type":"application/json", "Accept-Charset":"UTF-8"}

r = requests.get(url, params=PARAMS)
# r = requests.post(url, data={"sample":"data"}, headers=headers)
#print(r)

data = r.json()
print(data)