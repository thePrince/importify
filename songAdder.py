import requests
import json
import spotipy.util as util
import getArtistsFromLocal


def getIdsForArtists(listOfArtists):
    print 'getting the spotify ids for your artists (this may take a while)'

    ids = []
    for artist in listOfArtists:
        r = requests.get('http://api.spotify.com/v1/search?type=artist&q=' + artist, 80)
        if not 'artists' in r.json():
            continue
        items = r.json()['artists']['items']
        if len(items) == 0:
            continue
        # just get first artist.  this could cause unexpected results, if the intended artist is not the first result.
        ids.append(items[0]['id'])
    return ids

def getTopTracksForArtists(artistIdsList):
    print 'getting the top 5 tracks for each artist (this may take a while)'
    songIds = []
    with open('songIds.txt', 'w') as songIdsFile:
        for artistId in artistIdsList:
            url = 'https://api.spotify.com/v1/artists/' + str(artistId) + '/top-tracks?country=US'
            r = requests.get(url)
            tracks = r.json()['tracks']
            #limit to 2 songs per artist so you don't exceed spotify's 10,000 song limit
            counter = 0
            for song in tracks:
                if counter >= 5:
                    break
                songIdsFile.write(song['id'] + '\n')
                songIds.append(song['id'])
                counter += 1
    songIdsFile.close()
    return songIds

#currently not used, but it could be useful at some point
def getAlbumsForArtists(artistIdsList):
    print 'getting the albums for each artist'
    albumIds = []
    for artistId in artistIdsList:
        url = 'https://api.spotify.com/v1/artists/' + str(ID) + '/albums'
        r = requests.get(url)
        albums = r.json()['items']
        for album in albums:
            albumIds.append(album['id'])
    return albumIds

def addTracksToLibray(trackIds, username):
    print 'adding the tracks to your library (check progress in Spotify app)'
    #authServer must be running for this to work
    #shhhh don't give away the secret
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
        r = requests.put('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)
        i += 50
    #get the remainder after the last chunk of 50
    currTracks = ','.join(trackIds[i:])
    payload = {'ids': currTracks}
    r = requests.put('https://api.spotify.com/v1/me/tracks', headers=headers, params=payload)

def getUsername():
    name = raw_input('please enter your spotify username:')
    return name






def main():
    print 'starting the import pipeline'
    listOfArtists = getArtistsFromLocal.main()
    artistIds = getIdsForArtists(listOfArtists)
    trackIds = getTopTracksForArtists(artistIds)
    username = getUsername()
    addTracksToLibray(trackIds, username)
    print 'finished importing music.  please check your spotify to confirm.'

if __name__ == '__main__':
    main()