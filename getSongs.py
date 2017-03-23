#!/usr/bin/env python
import sys
import glob
import re

blackListWords = [' No. ', ' Disc ', 'www.', 'Op.', '.com', ' .net']
badChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '+', '@', ',', '!', '?', '~', '$', "'", '/', '#', '&']
def getSongs():
	pathsToMusic = ['/Volumes/FreeAgent Drive/Music']
	songMaps = []
	for path in pathsToMusic:
		count = 0
		try:
			#every artist
			for artistPath in glob.iglob(cleanStringForGlob(path) + '/*'):
				artist = cleanName(artistPath)
				count += 1
				for songPath in glob.iglob(cleanStringForGlob(artistPath) + '/*.m*'):
						songWithoutAlbum = songPath
				for albumPath in glob.iglob(cleanStringForGlob(artistPath) + '/*'):
					#songs/albums.  try catch later to deal with songs
					album = cleanName(albumPath)
					print album
					#cleanName(albumPath)
					
					#get the songs that are mp3, m4a etc
					#do also for FLAC, wav
					for songPath in glob.iglob(cleanStringForGlob(albumPath) + '/*.m*'):
						song = cleanSong(songPath)
						if song is None:
							continue
						songMaps.append({'artist': artist, 'album': album, 'song': song})
						#print artist + "  " + album + "  " + song
			    #print artist, so then run this script and > output to a file
		except Exception as e:
			print 'exception -- last passing file was: '
			#print songPath
			print e



def cleanStringForGlob(string):
	#b/c glob escapes special characters with brackets instead of backslash
	#special characters are * ? [ ] .
	newString = ''
	for char in string:
		if char == '*' or char == '?' or char == '[' or char == ']':
			newString += '[' + char + ']'
		else:
			newString += char
	return newString


def cleanName(namePath):
	actualName = ''
	cleanName = ''

	#get album from path
	reverseName = ''
	for char in namePath[::-1]:
		if char == '/':
			break
		reverseName += char
	if (reverseName == ''):
		return
	actualName = reverseName[::-1]
	return cleanse(actualName)


def cleanSong(songPath):
	actualTitle = ''

	## first parse path to get song part 
	cleanTitle = ''
	##OTHER TRACKLIST PATTERNS TO ACCOMODATE:
		# 02-title
		# 02title
		# 02 title
		#  _ 
		# 02.title
		# 02_title
		# 2.title
		# 02. title
	tracklistPattern = re.compile('. - ')
	if (tracklistPattern.search(songPath) is not None):
		withExt = tracklistPattern.split(songPath)[1]
	else:
		###TODO more robust song parsing
		return

	extPattern = re.compile('\.m.')
	if (extPattern.search(withExt) is not None):
		actualTitle = extPattern.split(withExt)[0]

	## get rid of special characters
	almostThere = ''
	for char in actualTitle:
		if char in badChars:
			almostThere += ' '
		else: 
			almostThere += char

	## get rid of parenthetical information
	parenthesesPattern = re.compile('\(.*\)')
	bracketsPattern = re.compile('\[.*\]')
	cleanTitle = parenthesesPattern.sub('', bracketsPattern.sub('', almostThere))
	return cleanTitle

def cleanse(string):
	cleaned = ''
	parenthesesPattern = re.compile('\(.*\)')
	bracketsPattern = re.compile('\[.*\]')
	string = parenthesesPattern.sub('', bracketsPattern.sub('', string))

	for char in string:
		if char in badChars:
			cleaned += ' '
		else: 
			cleaned += char
	return cleaned



if __name__ == '__main__':
	getSongs()
