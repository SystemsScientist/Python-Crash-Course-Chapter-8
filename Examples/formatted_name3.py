# formatted_name3.py, Chapter 8, Python Crash Course
# program returns and prints a full name

def get_formatted_name(first_name, last_name, middle_name = ''):
    """return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



