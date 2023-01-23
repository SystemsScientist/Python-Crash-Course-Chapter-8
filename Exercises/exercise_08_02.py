# exercise_08_02.py, Chapter 8, Python Crash Course
# 
# Favorite Book: Write a function called favorite_book()
# that accepts one parameter, book_title. The function should
# print a message, such as "One of my favorite books is
# Alice in Wonderland". Call the function, making sure to
# include a book title as an argument in the function
# call.

# use book_title instead of title for the parameter
def favorite_book(book_title):
    """display favorite book"""
    print("One of my favorite books is " + book_title.title() + ".")

favorite_book('Alice in Wonderland') 



