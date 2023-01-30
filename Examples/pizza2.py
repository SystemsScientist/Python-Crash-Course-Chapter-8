# pizza2.py, Chapter 8, Python Crash Course
# program prints pizza toppings

def make_pizza(*toppings):
    """summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')



