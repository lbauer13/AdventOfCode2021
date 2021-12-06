#!/usr/bin/env python3
import sys

# read file
numbers = []
inputs = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if not len(numbers):
            numbers = list(map(lambda x: int(x), line.rstrip().split(',')))
        else:
            inputs.append(list(map(lambda x: int(x), [ i for i in line.rstrip().split(' ') if i ])))

# get all boards
# first reverse list so that each board ends with an empty line
inputs.reverse()

# for each board, first index is lines and second is columns
# use more memory but less CPU
board = []
boards = []
for line in inputs:
    if len(line):
        board.append(line)
    else:
        # board is full
        boards.append(board)
        # next board
        board = []

def print_board(b):
    for l in b:
        for c in l:
            print(f' {c} ', end='')
        print("\n")

def board_has_empty(b):
    # check lines
    for l in b:
        if ''.join(map(lambda x: str(x), l)) == ''.join([ '*' ] * len(l)):
            return True
    # check columns
    for i in range(0, len(b[0])):
        col = [];
        for j in range(0, len(b[0])):
            col.append(b[j][i])
        if ''.join(map(lambda x: str(x), col)) == ''.join([ '*' ] * len(l)):
            return True
    return False

# draw numbers
def draw_numbers(mynumbers, myboards, until_last):
    for n in mynumbers:
        b = 0
        while b < len(myboards):
            board = myboards[b]
            found_number = False
            has_empty = False
            # lines
            for l in range(0, len(board)):
                while n in board[l]:
                    found_number = True
                    pos = board[l].index(n)
                    board[l][pos] = '*'

            if board_has_empty(board):
                #print_board(board)

                # return first winning board, or continue until last one
                if (len(myboards) == 1) or not until_last:
                    s = 0
                    for l in board:
                        s += sum([ i for i in l if i != '*' ])
                    return (n * s)
        
                del(myboards[b])
            else:
                b += 1

# check boards in expected order
# only for convenience and debug purpose
boards.reverse()

print ('Part 1 : ' + str(draw_numbers(numbers, boards, False)))

# no need to start over, some work has already been done
print ('Part 2 : ' + str(draw_numbers(numbers, boards, True)))
