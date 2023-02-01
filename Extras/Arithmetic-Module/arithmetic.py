# arithmetic.py, Chapter 8, Python Crash Course
# program computes two numbers

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def compute(num1, num2):
    print("\nCompute two numbers with +, -, *, and /: ")
    print("-------------------------------------------")
    add_two_numbers = add(num1, num2)
    print("\nnum1 + num2 = " + str(add_two_numbers))

    subtract_two_numbers = subtract(num1, num2)
    print("num1 - num2 = " + str(subtract_two_numbers))

    multiply_two_numbers = multiply(num1, num2)
    print("num1 * num2 = " + str(multiply_two_numbers))

    divide_two_numbers = divide(num1, num2)
    print("num1 / num2 = " + str(divide_two_numbers) + "\n")

compute(5, 5)
compute(6, 6)



