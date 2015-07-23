__author__ = 'Gabriel Fishman'

"""
RACING CHARS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/136/
You are given a file where each line is a section of a race track with obstructions, gates, and checkpoints.
Your task is to find a way to pass this track using the following information:

1. Each section contains either one single gate or one gate with a checkpoint.
2. You should drive only through gates or checkpoints.
3. You should drive through a checkpoint rather than a gate.
4. An obstruction is represented by a number sign "#".
5. A gate is represented by an underscore "_".
6. A checkpoint is represented by a letter C.

INPUT SAMPLE:

Your program should accept a path to a filename as its first argument. Each line of the file is a new section of a race
rack.

 1. #########_##
 2. ########C_##
 3. #######_####
 4. ######_#C###
 5. #######_C###
 6. #######_####
 7. ######C#_###
 8. ######C_####
 9. #######_####
10. #######_####

OUTPUT SAMPLE:

Print out the way of passing this race track starting from the first line in the file. Use a pipe "|" for the straight,
use a slash "/" for the left turn, and use a backslash "\" for the right turn.

 1. #########|##
 2. ########/_##
 3. #######/####
 4. ######_#\###
 5. #######_|###
 6. #######/####
 7. ######/#_###
 8. ######|_####
 9. #######\####
10. #######|####

CONSTRAINTS:

The number of lines in a file is 50.
The width of a section is 12 characters.
"""
import sys


def get_next_move(row, col, char_arr):
    if char_arr[row][col] == "C" or char_arr[row][col] == "_":
        if row == 0:
            char_arr[row][col] = "|"
            return True
        else:
            next_move_arr = []
            if char_arr[row - 1][col - 1] == "C":
                next_move_arr.append([-1, "\\"])
            if char_arr[row - 1][col] == "C":
                next_move_arr.append([0, "|"])
            if char_arr[row - 1][col + 1] == "C":
                next_move_arr.append([1, "/"])
            if char_arr[row - 1][col - 1] == "_":
                next_move_arr.append([-1, "\\"])
            if char_arr[row - 1][col] == "_":
                next_move_arr.append([0, "|"])
            if char_arr[row - 1][col + 1] == "_":
                next_move_arr.append([1, "/"])

            for n in next_move_arr:
                if get_next_move(row - 1, col + n[0], char_arr):
                    char_arr[row][col] = n[1]
                    return True
    else:
        return False

with open(sys.argv[1], 'r') as test_cases:
    char_arr = []
    for line in test_cases:
        line = line.strip()
        char_arr.append(list(line))

last_row = len(char_arr) - 1
for i in range(0, len(char_arr[0])):
    if char_arr[last_row][i] == "C" or char_arr[last_row][i] == "_":
        get_next_move(last_row, i, char_arr)

for line in char_arr:
    print "".join(line)

