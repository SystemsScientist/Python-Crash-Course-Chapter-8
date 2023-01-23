# pets3.py, Chapter 8, Python Crash Course
# program makes a function call and produces
# unexpected results

def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')



