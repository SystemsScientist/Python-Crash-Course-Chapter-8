# exercise_08_10.py, Chapter 8, Python Crash Course
# 
# Great Magicians: Start with a copy of your program
# from exercise_08_09.py. Write a function called
# make_great() that modifies the list of magicians by
# adding the phrase "the Great" to each magician's
# name. Call show_magicians() to see that the list
# has actually been modified.


def show_magicians(great_magicians):
    """print list of great magicians"""
    print("\nList of Great Magicians: ")
    for great_magician in great_magicians:
        print("\t" + great_magician)


def make_great(magicians, great_magicians):
    """print list of magicians"""
    print("\nList of Magicians: ")
    while magicians:
        current_magician = magicians.pop()
        print("\t" + current_magician.title())
        great_magicians.append("the Great " + current_magician.title())


magicians = ['harry anderson', 'penn and teller',
             'david copperfield', 'harry houdini',
             'ricky jay', 'david blaine']
great_magicians = []

make_great(magicians, great_magicians)
show_magicians(great_magicians)




