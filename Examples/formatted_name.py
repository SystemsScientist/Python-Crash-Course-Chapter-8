# formatted_name.py, Chapter 8, Python Crash Course
# program returns and prints a full name

def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)



