# exercise_08_09.py, Chapter 8, Python Crash Course
# 
# Magicians: Make a list of magicians' names. Pass the list 
# to a function called show_magicians(), which prints the name
# of each magician in the list

def show_magicians(magicians):
    """print list of magicians"""
    print("\nList of Magicians: ")
    for magician in magicians:
        print("\t" + magician.title())

magicians = ['harry anderson', 'penn and teller', 
             'david copperfield', 'harry houdini', 
             'ricky jay']
show_magicians(magicians)



