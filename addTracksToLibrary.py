import requests
import spotipy
import spotipy.util as util


tracks = []
with open('songIds.txt', 'r') as ids:
    for line in ids:
        tracks.append(line.strip())
ids.close()

rt = list(reversed(tracks))
#get auth code/token
scope = 'user-library-modify'
#might first need to set environment vars for spotifizer
#export SPOTIPY_CLIENT_ID='aaa5fcf874084f88a7c1e00ba8002722'
#export SPOTIPY_CLIENT_SECRET='fee54176991842438e30b4606d50bd73'
#export SPOTIPY_REDIRECT_URI='http://localhost:8000'
token = util.prompt_for_user_token('princeBolkonsky', scope)


#use token to make changes to Spotify account
headers = {'Authorization': 'Bearer ' + token}
i = 0
while i < len(rt):#-50 :
    #currTracks = ','.join(rt[i : i + 50])
    #THIS STILL ISN'T BEING ADDED?  WHY?  AND WHY DOES THE BULK ADD STOP WORKING ~THE R ARTISTS? AND WHY DID DOING THEM INDIVIDUALLY, REVERSED, ADD NEW SONGS?
    #currTracks = '7r6KgeFLSGJqbu90KJg1Bv'
    currTracks = rt[i]
    payload = {'ids': currTracks}
    r = requests.put('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)
    #i += 50
    i += 1
    if '7r6KgeFLSGJqbu90KJg1Bv' == currTracks:
        print currTracks
        print i
        print r
        print r.content
    #JUST TO TEST THE ONE SONG
    print r

#currTracks = ','.join(rt[i:])
#payload = {'ids': currTracks}
#r = requests.put('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)
#print r

