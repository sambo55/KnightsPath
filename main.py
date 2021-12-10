# !/usr/bin/env python3

def move_knight(knight_pos, move_num):
    """
    Function that takes a knight position tuple and a move_number.
    Each move_number represents a move the knight can make
    """
    if move_num == 0:
        return knight_pos[0] - 2, knight_pos[1] + 1
    if move_num == 1:
        return knight_pos[0] - 2, knight_pos[1] - 1
    if move_num == 2:
        return knight_pos[0] - 1, knight_pos[1] + 2
    if move_num == 3:
        return knight_pos[0] - 1, knight_pos[1] - 2
    if move_num == 4:
        return knight_pos[0] + 2, knight_pos[1] + 1
    if move_num == 5:
        return knight_pos[0] + 2, knight_pos[1] - 1
    if move_num == 6:
        return knight_pos[0] + 1, knight_pos[1] + 2
    if move_num == 7:
        return knight_pos[0] + 1, knight_pos[1] - 2


def find_legal_moves(knight_pos, move_list=None):

    """
    knight_pos is a tuple where each element is between 0 and 7
    this represents each square on the chessboard
    return list of squares that are 1 move away
    """

    legal_moves = []

    if not move_list:
        move_list = [i for i in range(8)]

    for move in move_list:

        move_outcome = move_knight(knight_pos, move)
        if (min(move_outcome) >= 0) and (max(move_outcome) <= 7):
            legal_moves.append(move)

    return legal_moves


def get_branches(position_list, target):

    """
    Take a list of knight_positions and a target
    Loop through each position
    Loop through each legal move
    Create a list with the new move appended
    So we will end up with a list of all branches that have been
    traversed
    If we reach the target square then we return the branch that ended at
    the target as the shortest path.
    """

    branch_list = []

    for pos in position_list:

        for move in find_legal_moves(pos[-1]):

            branch = []
            branch.extend(pos)

            r = move_knight(pos[-1], move)
            branch.append(r)

            if r == target:
                return branch

            branch_list.append(branch)

    return branch_list


def get_shortest_path(starting_square, target_square):

    """
    Take a starting square and a target square
    Get list of possible states after 1 move
    If target not in possible states then try all 1 step moves from
    all previously reached states.
    Repeat until target is reached
    Guarantees shortest path as we are iterating through all 1-move, 2-move,
    3-move... combos
    """
    shortest_path = [starting_square]

    move_list = get_branches([shortest_path], target_square)

    while target_square not in move_list:

        move_list = get_branches(move_list, target_square)

    shortest_path.extend(move_list)

    return shortest_path


def print_shortest_path(shortest_path):

    """
    Convert results of shortest path algorithm back to chess notation and
    print result
    """
    string_list = [translate_output(pos) for pos in shortest_path]
    print(" ".join(string_list))


# Dictionaries for mapping between number and chess notation
num_to_letter = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D',
    4: 'E', 5: 'F', 6: 'G', 7: 'H'
}

letter_to_num = {v: k for k, v in num_to_letter.items()}


def parse_input(square_str):
    """
    Convert chess square notation to tuple of ints [0-7]
    """
    x0 = letter_to_num[square_str[0].upper()]
    x1 = int(square_str[1]) - 1

    return x0, x1


def translate_output(square_tuple):
    """
    Convert position tuple back to chess square notation
    """
    return num_to_letter[square_tuple[0]] + str(square_tuple[1] + 1)


def get_input():
    """
    Take multiline inputs from user and return a list where each element is
    a line of input
    """

    input_list = []
    while True:
        inp = input()
        if inp:
            input_list.append(inp)
        else:
            break

    return input_list


lines = get_input()

for line in lines:

    starting_square = parse_input(line.split(' ')[0])
    target_square = parse_input(line.split(' ')[1])

    shortest_path = get_shortest_path(starting_square, target_square)
    print_shortest_path(shortest_path)
