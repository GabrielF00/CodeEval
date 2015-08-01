__author__ = 'Gabriel Fishman'

"""
MULTIPLES OF A NUMBER
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/18/

Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to
x. Do not use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of two integers, one list per line.
E.g.

* 13,8
* 17,16

OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

* 16
* 32
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        numArr = test_case.strip().split(",")
        x = int(numArr[0])
        n = int(numArr[1])
        result = n
        while result < x:
            result += n
        print result
