# exercise_08_05.py, Chapter 8, Python Crash Course
# 
# Cities: Write a function called describe_city() that
# accepts the name of a city and its country. The
# function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the
# country a default value. Call your function for three
# different cities, at least one of which is not in the
# default country.

def describe_city(city, country = "America"):
    print("\n" + city.title() + " is in " + country.title() + ".")

describe_city(city = 'reykjavik', country = 'iceland')
describe_city(city = 'minneapolis')
describe_city(city = 'stockholm', country = 'sweden')
describe_city(city = 'dallas')



