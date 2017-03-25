import sys
import glob
import re

#TODO add handling for more unicode (e.g. mo:torhead)

blackListWords = [' no. ', ' disc ', 'www.', 'op.', '.com', ' .net', 'feat.', 'complete discography', 'discography']
badChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '+', '@', ',', '!', '?', '~', '$', "'", '/', '#', '&']

def getSongs(path):
	artists = []
	songMaps = []
	try:
		for artistPath in glob.iglob(cleanStringForGlob(path) + '/*'):
			artist = cleanName(artistPath)
			artists.append(artist)

			#currently i'm just using artists to add music
			#in the future, maybe use this to make the program more accurate
			# for songPath in glob.iglob(cleanStringForGlob(artistPath) + '/*.m*'):
			# 		songWithoutAlbum = songPath
			# for albumPath in glob.iglob(cleanStringForGlob(artistPath) + '/*'):
			# 	#songs/albums.  try catch later to deal with songs
			# 	album = cleanName(albumPath)
			# 	print album
			# 	#cleanName(albumPath)
				
			# 	#get the songs that are mp3, m4a etc
			# 	#do also for FLAC, wav
			# 	for songPath in glob.iglob(cleanStringForGlob(albumPath) + '/*.m*'):
			# 		song = cleanSong(songPath)
			# 		if song is None:
			# 			continue
			# 		songMaps.append({'artist': artist, 'album': album, 'song': song})
			# 		#print artist + "  " + album + "  " + song
	except Exception as e:
		print 'exception -- last passing file was: '
		#print songPath
		print e
	return artists



def cleanStringForGlob(string):
	#glob escapes special characters with brackets instead of backslash
	#special characters are * ? [ ], so  if the string contains any of these wrap them in brackets.
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

	#get artist (or album, song) from the path by looping backwards until you reach a '/'
	#example: '~/music/artistName' would return 'artistName'
	reverseName = ''
	for char in namePath[::-1]:
		if char == '/':
			break
		reverseName += char
	if (reverseName == ''):
		return
	actualName = reverseName[::-1].lower()
	return cleanse(actualName)

#not currently used
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
	#TODO make this a separate method
	parenthesesPattern = re.compile('\(.*\)')
	bracketsPattern = re.compile('\[.*\]')
	string = parenthesesPattern.sub('', bracketsPattern.sub('', string))

	for char in string:
		if char in badChars:
			cleaned += ' '
		else: 
			cleaned += char
	for word in blackListWords:
		if word in cleaned:
			cleaned = cleaned.replace(word, ' ')
	return cleaned

def main():
	print 'please enter the path to your music directory'
	print 'example: /Volumes/FreeAgent Drive/Music'
	print 'the Music directory should contain Artist folders, and those should contain song files and/or Album folders, which should contain song files'
	print 'example: /Volumes/FreeAgent Drive/Music/Mastodon/Leviathan/Aqua Dementia.mp3'
	print ' '
	pathToMusic = raw_input('music directory path: ')
	artists = getSongs(pathToMusic)
	return artists


if __name__ == '__main__':
	main()
