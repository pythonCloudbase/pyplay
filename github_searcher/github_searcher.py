import requests

get = input("Name of the user: ")

if (get==""):
    get = "fanbyprinciple"

url= "https://api.github.com/users/" + get + "/following"
# add your token here as PARAMS
# PARAMS = {username: token}
# headers={"content-type":"application/json", "Accept-Charset":"UTF-8"}

r = requests.get(url, params=PARAMS)
# r = requests.post(url, data={"sample":"data"}, headers=headers)
#print(r)

data = r.json()

# star_url = data[0]["starred_url"]
# print(star_url.split("{")[0])
# r_star = requests.get(star_url)
# data_star = r_star.json()
# print(data_star)

# for d in data[0]:
#     print(d)

for d in data:
    #followers = d["followers"]
    # blog = d["blog"]
    starred_url = d["starred_url"]
    name = d["login"]
    print(name, ":")
    print(" starred_url: ", starred_url)
    print("#################################")
