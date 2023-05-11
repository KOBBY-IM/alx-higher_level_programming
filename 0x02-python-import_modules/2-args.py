#!/usr/bin/python3

if __name__ == "__main__":
# Import the sys module
    import sys

# Get the number of arguments passed to the program
    num_args = len(sys.argv) - 1

# If no arguments were passed, print "No arguments"
    if num_args == 0:
        print("No arguments")
    elif num_args == 1:
        print("1 argument:")

# Otherwise, print the number of arguments followed by a colon,
# followed by a new line, followed by one line per argument:
# the position of the argument (starting at 1) followed by a colon,
# followed by the argument value and a new line
    else:
        print("{} arguments:".format(num_args))
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
