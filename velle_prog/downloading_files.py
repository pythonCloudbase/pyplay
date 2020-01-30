import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: ', exc)

downloaded_file = open('Romeo&Juliet.txt', 'wb')

for chunk in res.iter_content(100000):
        downloaded_file.write(chunk)

downloaded_file.close()