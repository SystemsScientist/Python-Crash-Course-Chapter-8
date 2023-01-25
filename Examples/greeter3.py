# greeter3.py, Chapter 8, Python Crash Course
# program greets a person

def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name

    return full_name.title()

# this is an infinite loop! do not run the program!
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")



