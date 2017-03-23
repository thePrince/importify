import requests
import json

them = []
with open('artistIds.txt', 'r') as ids:
    for line in ids:
        them.append(line.strip())
ids.close()

for ID in them:
    url = 'https://api.spotify.com/v1/artists/' + str(ID) + '/top-tracks?country=US'
    r = requests.get(url)
    tracks = r.json()['tracks']
    if ID == '3GzWhE2xadJiW8MqRKIVSK':
        print 'getting underoath'
        for song in tracks:
            print song['id']
    #for song in tracks:
     #   print song['id'] # > songIds.txt