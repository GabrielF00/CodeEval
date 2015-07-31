__author__ = 'Gabriel Fishman'

"""
CHALLENGE DESCRIPTION:

There are two details on a M*N checkered field. The detail X covers several (at least one first cell) cells in each
line. The detail Y covers several (at least one last cell) cells. Each cell is either fully covered with a detail or not.

For example:

X X * Y Y
X X X * Y
X * * Y Y
X X * * Y

Also, the details may have cavities (or other complex structures).
Please see example below (the detail Y is one detail):

X X X * Y Y Y Y
X * * * Y * * Y
X X * * Y Y Y Y
X * * * * * Y Y
X X * * * * Y Y

The detail Y starts moving left (without any turn) until it bumps into the X detail at least with one cell. Determine by
how many cells the detail Y will be moved.

INPUT SAMPLE:

The first argument is a file with different test cases. Each test case contains a matrix the lines of which are
separated by comma. (Empty cells are marked as ".")

For example:

1. XX.YY,XXX.Y,X..YY,XX..Y
2. XXX.YYYY,X...Y..Y,XX..YYYY,X.....YY,XX....YY
3. XX...YY,X....YY,XX..YYY,X..YYYY
4. XXYY,X..Y,XX.Y

OUTPUT SAMPLE:

Print out the number of cells the detail Y will be moved.

For example:

1. 1
2. 1
3. 2
4. 0
"""

import re
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        lines = test_case.strip().split(',')
        min_distance = 99
        for line in lines:
            m = re.match(r'^[X\.]*X(\.*)[Y\.]*Y*$', line)
            if len(m.group(1)) < min_distance:
                min_distance = len(m.group(1))
        print min_distance

