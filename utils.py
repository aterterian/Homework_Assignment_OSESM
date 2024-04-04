import math


def print_christmas_tree(height):
    # Print a christmas tree in a choosable height

    for i in range(1, height + 1):  # Define iterations (rows) based on the inputted height
        print(" " * (height-i), end="")  # Print the right amount of spaces in order to shape the tree form
        for j in range(1, i + 1):  # Define the amount of iterations (stars) necessary for the specific row
            print("*", end=" ")
        print("")  # Next line
    width = height + height-1
    stem_height = math.ceil(height*1/6)
    stem_width = math.ceil(height/5)
    for i in range(1, stem_height+1):  # Define iterations (height) of the stem
        print(" " * math.floor((width/2)-stem_width+1), end="")  # Print the right amount of spaces in order to center the stem
        print("* " * stem_width)


print_christmas_tree(5)


