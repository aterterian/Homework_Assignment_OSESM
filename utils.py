import math
import random


def print_christmas_tree(height):
    # Print a christmas tree in a choosable height
    if height <= 1:
        print("Leave the tree to grow a bit more!")
    else:
        for i in range(1, height + 1):  # Define iterations (rows) based on the inputted height
            print(" " * (height - i), end="")  # Print the right amount of spaces in order to shape the tree form
            for j in range(1, i + 1):  # Define the amount of iterations (stars) necessary for the specific row
                if random.random() < 0.15:  # Probability of placing a festive ball
                    print("o", end=" ")
                else:
                    print("*", end=" ")
            print("")  # Next line
        width = height + height - 1
        stem_height = math.ceil(height * 1 / 6)
        stem_width = math.ceil(height / 5)
        for i in range(1, stem_height + 1):  # Define iterations (height) of the stem
            print(" " * math.floor((width / 2) - stem_width + 1), end="")  # Print the right amount of spaces in order to center the stem
            print("| " * stem_width)


def print_diamond(size, edge_symbol='*', inner_symbol=' '):  # Gives the option to change the diamonds appearence, and also sets a standard appearence
    if size <= 1:
        print("Why would you want such a small diamond?")
    else:
        for i in range(size):
            if i == 0:
                print(" " * (size - i - 1) + edge_symbol)
            else:
                print(" " * (size - i - 1) + edge_symbol + inner_symbol * (2 * i - 1) + edge_symbol)
        for i in range(size - 2, -1, -1):
            if i == 0:
                print(" " * (size - i - 1) + edge_symbol)
            else:
                print(" " * (size - i - 1) + edge_symbol + inner_symbol * (2 * i - 1) + edge_symbol)


#  Add a test function to check if the testing works

def subtract(a, b):

    return a-b

