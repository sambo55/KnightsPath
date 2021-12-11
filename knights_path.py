# !/usr/bin/env python3

from functions import get_input, parse_input, print_shortest_path, \
    get_shortest_path
# Get input from user
lines = get_input()

# For each line input by user
# Parse the starting and target squares
# Run get shortest path
# Print result

for line in lines:
    starting_square = parse_input(line.split(' ')[0])
    target_square = parse_input(line.split(' ')[1])

    # check the 0-move case
    if starting_square == target_square:
        print_shortest_path([starting_square, target_square])

    else:
        shortest_path = get_shortest_path(starting_square, target_square)
        print_shortest_path(shortest_path)
