# !/usr/bin/env python3

def move_knight(knight_pos, move_num):
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


def get_starting_moves(square, target):

    position_list = []

    for m in find_legal_moves(square):

        r = move_knight(square, m)
        position_list.append([r])

        if r == target:
            return position_list

    return position_list


def get_branches(position_list, target):

    branch_list = []

    for pos in position_list:

        for m in find_legal_moves(pos[-1]):

            branch = []
            branch.extend(pos)

            r = move_knight(pos[-1], m)
            branch.append(r)

            if r == target:
                return branch

            branch_list.append(branch)

    return branch_list



num_to_letter = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
}

letter_to_num = {v: k for k, v in num_to_letter.items()}


def parse_input(square_str):
    x0 = letter_to_num[square_str[0].upper()]
    x1 = int(square_str[1]) - 1

    return x0, x1


def translate_output(square_tuple):
    return num_to_letter[square_tuple[0]] + str(square_tuple[1] + 1)


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

for line in lines:

    if len(line) != 5:
        'incorrect input format'
    elif line[2] != ' ':
        'incorrect input format: please put a space between the two squares'
    else:
        starting_square_str = line.split(' ')[0]
        target_square_str = line.split(' ')[1]

        starting_square = parse_input(starting_square_str)
        target_square = parse_input(target_square_str)

        pos_list = get_starting_moves(starting_square, target_square)

        while target_square not in pos_list:
            pos_list = get_branches(pos_list, target_square)

        shortest_path = starting_square_str
        for p in pos_list:
            shortest_path += ' '
            shortest_path += translate_output(p)

        print(shortest_path)

# for line in lines
# parse the first part as the starting square and the second as the target


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
