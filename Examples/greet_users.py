# greeter_users.py, Chapter 8, Python Crash Course
# program prints a list

def greet_users(names):
    """print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



