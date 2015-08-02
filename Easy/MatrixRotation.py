__author__ = 'Gabriel Fishman'
"""
MATRIX ROTATION
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/178/
You are given a 2D N x N matrix. Each element of the matrix is a letter: from 'a' to 'z'. Your task is to rotate the
matrix 90 degrees clockwise:

a b c        g d a
d e f  =>    h e b
g h i        i f c

INPUT SAMPLE:

The first argument is a file that contains 2D N x N matrices, presented in a serialized form (starting from the
upper-left element), one matrix per line. The elements of a matrix are separated by spaces.

For example:

* a b c d
* a b c d e f g h i j k l m n o p
* a b c d e f g h i

OUTPUT SAMPLE:

Print to stdout matrices rotated 90 degrees clockwise in a serialized form (same as in the input sample).

For example:

* c a d b
* m i e a n j f b o k g c p l h d
* g d a h e b i f c
"""

import math
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        flat_list = test_case.strip().split(" ")
        row_size = int(math.sqrt(len(flat_list)))
        # Convert the flat list into a matrix.
        matrix = [[flat_list[j + i] for i in range(row_size)] for j in range(0, len(flat_list), row_size)]
        # This reads every column in the matrix from bottom to top and transposes that column into a row of the result
        transposed_matrix = [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]
        output = ""
        for row in transposed_matrix:
            for i in range(len(row)):
                output += " "
                output += row[i]
        print output.lstrip()
