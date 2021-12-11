# Dictionaries for mapping between number and chess notation

num_to_letter = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D',
    4: 'E', 5: 'F', 6: 'G', 7: 'H'
}

letter_to_num = {v: k for k, v in num_to_letter.items()}


def get_input() -> list:
    """
    Take multiline inputs from user and return a list where each element is
    a line of input
    """

    input_list = []
    while True:

        inp = input('Enter two chess squares separated by a space: ')

        if inp:
            check_input(inp)
            input_list.append(inp)
        else:
            break

    return input_list


def check_input(inp):
    """
    Want to check that each input line is valid
    Check that it has five characters
    check that it has two two character pieces separated by a space
    check that each two character sequence is a valid chess piece
    """
    val_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    val_nums = ['1', '2', '3', '4', '5', '6', '7', '8']

    if len(inp) != 5:
        raise ValueError('Input must be two chess squares separated by a space')

    if inp[2] != ' ':
        raise ValueError('Input must be two chess squares separated by a space')

    if inp[0].upper() not in val_chars:
        raise ValueError('{}{} not a valid chess square'.format(inp[0], inp[1]))

    if inp[1] not in val_nums:
        raise ValueError('{}{} not a valid chess square'.format(inp[0], inp[1]))

    if inp[3].upper() not in val_chars:
        raise ValueError('{}{} not a valid chess square'.format(inp[3], inp[4]))

    if inp[4] not in val_nums:
        raise ValueError('{}{} not a valid chess square'.format(inp[3], inp[4]))


def parse_input(square_str: str) -> tuple[int, int]:
    """
    Convert chess square notation to tuple of ints [0-7]
    """
    x0 = letter_to_num[square_str[0].upper()]
    x1 = int(square_str[1]) - 1

    return x0, x1


def translate_output(square_tuple: tuple) -> str:
    """
    Convert position tuple back to chess square notation
    """
    return num_to_letter[square_tuple[0]] + str(square_tuple[1] + 1)


def move_knight(knight_pos: tuple[int, int], move_num: int) -> tuple[int, int]:
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


def get_branches(position_list: list, target: tuple[int, int]) -> list:
    """
    Take a list of knight_positions and a target
    Loop through each position
    Loop through each move
    Create a list with the new move appended if move is legal
    So we will end up with a list of all branches that have been
    traversed
    If we reach the target square then we return the branch that ended at
    the target as the shortest path.
    """

    branch_list = []

    for pos in position_list:

        for move in range(8):

            branch = []
            branch.extend(pos)

            r = move_knight(pos[-1], move)

            # check move is legal
            if (min(r) >= 0) and (max(r) <= 7):
                branch.append(r)
            else:
                continue

            if r == target:
                return branch

            branch_list.append(branch)

    return branch_list


def get_shortest_path(starting_square: tuple[int, int], target_square: tuple[
    int, int]) -> list:
    """
    Take a starting square and a target square
    Get list of possible states after 1 move
    If target not in possible states then try all 1 step moves from
    all previously reached states.
    Repeat until target is reached
    Guarantees shortest path as we are iterating through all 1-move, 2-move,
    3-move... combos
    """

    move_list = get_branches([[starting_square]], target_square)

    while target_square not in move_list:
        move_list = get_branches(move_list, target_square)

    return move_list


def print_shortest_path(shortest_path: list):
    """
    Convert results of shortest path algorithm back to chess notation and
    print result
    """
    string_list = [translate_output(pos) for pos in shortest_path]
    print(" ".join(string_list))
