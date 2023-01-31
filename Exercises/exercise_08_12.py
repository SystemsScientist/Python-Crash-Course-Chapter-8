# exercise_08_12.py, Chapter 8, Python Crash Course
# 
# Sandwiches: Write a function that accepts a list of items
# a person wants on a sandwich. The function should have one
# parameter that collects as many items as the function call
# provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times,
# using a different number of arguments each time.

# note: these are actual sandwiches I eat for lunch
def make_sandwich(*items):
    print("\nMaking a sandwich with the following toppings: ")
    for item in items:
        print("\t- " + item.title())

make_sandwich('mustard','mayonnaise', 'provolone cheese', 'roast beef')
make_sandwich('guacamole', 'mayonnaise', 'sharp chedder cheese', 'turkey')
make_sandwich('guacamole', 'mayonnaise', 'pepper jack cheese', 'chicken')



