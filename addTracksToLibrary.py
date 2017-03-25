import requests
import spotipy
import spotipy.util as util


trackIds = []
with open('songIds.txt', 'r') as ids:
    for line in ids:
        trackIds.append(line.strip())
ids.close()

#authServer must be running for this to work
#shhhh don't tell give away the secret
username = 'princeBolkonsky'
client_id='aaa5fcf874084f88a7c1e00ba8002722'
client_secret='fee54176991842438e30b4606d50bd73'
redirect_uri='http://localhost:8000'
scope = 'user-library-modify'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
headers = {'Authorization': 'Bearer ' + token}


#spotify's api allows up to 50 songs to be added with a single request
i = 0
while i < len(trackIds)-50:
    currTracks = ','.join(trackIds[i : i + 50])
    payload = {'ids': currTracks}
    r = requests.delete('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)
    i += 50
#get the remainder after the last chunk of 50
currTracks = ','.join(trackIds[i:])
payload = {'ids': currTracks}
r = requests.delete('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)

