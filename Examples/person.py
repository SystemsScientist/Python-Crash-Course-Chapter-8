# person.py, Chapter 8, Python Crash Course
# program returns and prints a dictionary

def build_person(first_name, last_name):
    """return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)



