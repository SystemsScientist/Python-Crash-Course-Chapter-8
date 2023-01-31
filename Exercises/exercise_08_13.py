# exercise_08_13.py, Chapter 8, Python Crash Course
# 
# User Profile: Start with a copy of user_profile.py
# from page 153, or user_profile.py located in the 
# Examples/ directory. 
#
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other 
# key-value pairs that describe you.

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('matt', 'johnson',
                             profession = 'embedded software engineer',
                             location = 'university of st thomas',
                             field = 'software engineering')

print(user_profile)



