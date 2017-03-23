import requests
import json

a = []
with open('artists.txt', 'r') as artists:
    for line in artists:
        a.append(line.strip())
artists.close()

for artist in a:
    r = requests.get('http://api.spotify.com/v1/search?type=artist&q=' + 'underoath', 80)
    if not 'artists' in r.json():
        continue
    items = r.json()['artists']['items']
    if len(items) == 0:
        continue
    print items[0]['id'] #, so then > this to artistIds.txt
