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



