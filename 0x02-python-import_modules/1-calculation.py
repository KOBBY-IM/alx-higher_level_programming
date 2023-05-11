#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add, sub, mul, and div functions from the calculator_1.py file
    from calculator_1 import add, sub, mul, div

    # Assign the value 10 to a variable called a
    a = 10

    # Assign the value 5 to a variable called b
    b = 5

    # Print the sum of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Print the difference of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Print the product of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Print the quotient of a and b
    print("{} / {} = {}".format(a, b, div(a, b)))
