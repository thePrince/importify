import requests
import json

them = []
with open('artistIds.txt', 'r') as ids:
    for line in ids:
        them.append(line.strip())
ids.close()

for ID in them:
    url = 'https://api.spotify.com/v1/artists/' + str(ID) + '/albums'
    r = requests.get(url)
    results = r.json()['items']
    for album in results:
        print album['id']