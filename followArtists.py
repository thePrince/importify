import requests
import spotipy
import spotipy.util as util

#get auth code/token
scope = 'user-follow-modify'

#might first need to set environment vars
#export SPOTIPY_CLIENT_ID='aaa5fcf874084f88a7c1e00ba8002722'
# export SPOTIPY_CLIENT_SECRET='fee54176991842438e30b4606d50bd73'
#export SPOTIPY_REDIRECT_URI='http://localhost:8000'
token = util.prompt_for_user_token('princeBolkonsky', scope)

#use token to make changes to Spotify account
headers = {'Authorization': 'Bearer ' + token}
payload = {'type': 'artist', 'ids': '2aaLAng2L2aWD2FClzwiep'}
r = requests.put('https://api.spotify.com/v1/me/following', headers=headers, params=payload)
print r