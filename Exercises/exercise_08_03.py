# exercise_08_03.py, Chapter 8, Python Crash Course
# 
# T-Shirt: Write a function called make_shirt() that
# accepts a size and the text of a message that should
# be printed on the shirt. The function should print a
# sentence summarizing the size of the shirt and the
# message printed on it. 
#
# Call the function once using positional arguments
# to make a shirt. Call the function a second time
# using keyword arguments.

def make_shirt(size, text):
    print("\nYour " + size + " shirt says '" + text + "'.")

make_shirt('large', 'You are here!')                # positional arguments
make_shirt(size = 'large', text = 'You are here!')  # keyword arguments



