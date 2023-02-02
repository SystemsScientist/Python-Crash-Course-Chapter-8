# compute.py, Chapter 8, Python Crash Course
# program computes the absolute number and the
# square of a number

def compute_absolute_number(num):
    if num < 0:
        num = num * -1;

    return num;


def compute_square_number(num):
    return num * num


def compute(num):
    print("\nCompute the absolute and square of a number: ")
    print("-----------------------------------------------")
    abs_num = compute_absolute_number(num)
    print("\nThe absolute number of num is: " + str(abs_num))

    square_num = compute_square_number(num)
    print("The square number of num is: " + str(square_num) +"\n")

compute(-4)
compute(-9.17)



