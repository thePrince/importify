import requests
import json


def getIdsForArtists(artistNamesFile):
    a = []
    with open(artistNamesFile, 'r') as artists:
        for line in artists:
            a.append(line.strip())
    artists.close()

    ids = []
    for artist in a:
        r = requests.get('http://api.spotify.com/v1/search?type=artist&q=' + artist, 80)
        counter += 1
        if not 'artists' in r.json():
            continue
        items = r.json()['artists']['items']
        if len(items) == 0:
            continue
        # just get first artist.  this could cause unexpected results, if the intended artist is not the first result.
        #to write these to a file, just put print statement here and > this script to the file
        ids.append(items[0]['id'])
    return ids

def getTopTracksForArtists(artistIdsList):
    songIds = []
    for artistId in artistIdsList:
        url = 'https://api.spotify.com/v1/artists/' + str(artistId) + '/top-tracks?country=US'
        r = requests.get(url)
        tracks = r.json()['tracks']
            for song in tracks:
                songIds.append(song['id'])
    return songIds

def getAlbumsForArtists(artistIdsList):
    albumIds = []
    for artistId in artistIdsList:
        url = 'https://api.spotify.com/v1/artists/' + str(ID) + '/albums'
        r = requests.get(url)
        albums = r.json()['items']
        for album in albums:
            albumIds.append(album['id'])
    return albumIds






def main():
    ids = getIdsForArtists('artists.txt')
    print ids

if __name__ == '__main__':
    main()