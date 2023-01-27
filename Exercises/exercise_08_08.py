# exercise_08_08.py, Chapter 8, Python Crash Course
# 
# User Albums: Start with your program from exercise_08_07.py.
# Write a while loop that allows users to enter an album's
# artist and title. Once you have that information, call
# make_album() with the user's input and print the dictionary
# that's created. Be sure to include a quit value in the while
# loop. 

def make_album(artist_name, album_title):
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    return album

while True:
    print("\nPlease enter your favorite Artist name and Album title: ")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    artist_album = make_album(artist_name, album_title)
    print(artist_album)

print("\nThanks for using this program. Have a wonderful day!\n")



