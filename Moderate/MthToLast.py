__author__ = 'Gabriel Fishman'
"""
MTH TO LAST ELEMENT

CHALLENGE DESCRIPTION:
See: https://www.codeeval.com/open_challenges/10/

Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space delimited characters followed by an
integer. The integer represents an index in the list (1-based), one per line.

For example:

* a b c d 4
* e f g h 2

OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of
elements in the list, ignore that input.

For example:

* a
* g
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num_arr = test.strip().split(" ")
        m = int(num_arr.pop())
        if m <= len(num_arr):
            print num_arr[len(num_arr) - m]

