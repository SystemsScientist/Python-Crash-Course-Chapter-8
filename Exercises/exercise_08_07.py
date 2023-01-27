# exercise_08_07.py, Chapter 8, Python Crash Course
# 
# Album: Write a function called make_album() that
# builds a dictionary describing a music album. The
# function should take in an artist name and an album
# title, and it should return a dictionary containing
# these two pieces of information. Use the function 
# to make three dictionaries representing different
# albums. Print each return value to show that the 
# dictionaries are storing the album information
# correctly.

def make_album(artist_name, album_title):
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    return album

print("List of Dictionaries of Artists and Albums: ")
print("--------------------------------------------")

artist_album = make_album(artist_name = 'dream theater', album_title = 'awake')
print(artist_album)

artist_album = make_album(artist_name = 'pink floyd', album_title = 'wish you were here')
print(artist_album)

artist_album = make_album(artist_name = 'joe satriani', album_title = 'the extremist')
print(artist_album)

# Add an optional parameter to make_album() that
# allows you to store the number of tracks on an
# album. If the calling line includes a value for
# the number of tracks, add that value to the album's
# dictionary. Make at least one new function call 
# that includes the number of tracks on an album.

def make_album(artist_name, album_title, number_of_tracks = ''):
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

print("\nList of Dictionaries of Artists and Albums: ")
print("----------------------------------------------")

artist_album = make_album(artist_name = 'michael jackson', album_title = 'thriller', number_of_tracks = 7)
print(artist_album)



