# exercise_08_06.py, Chapter 8, Python Crash Course
# 
# City Names: Write a function called city_country()
# that takes in the names of a city and its country.
# The function should return a string formatted like
# this:
#
#       Santiago, Chile
#
# Call your function with at least three city-country
# pairs, and print the value that's returned

def city_country(city, country):
    return city.title() + ', ' + country.title()

print("List of Cities and Countries: ")
city_country_pair = city_country(city = 'santiago', country = 'chile')
print("\t" + city_country_pair)

city_country_pair = city_country(city = 'paris', country = 'france')
print("\t" + city_country_pair)

city_country_pair = city_country(city = 'cairo', country = 'egypt')
print("\t" + city_country_pair)



