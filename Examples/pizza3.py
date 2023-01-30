# pizza3.py, Chapter 8, Python Crash Course
# program prints pizza toppings

def make_pizza(size, *toppings):
    """summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



