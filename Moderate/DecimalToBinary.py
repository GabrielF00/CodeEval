__author__ = 'Gabriel Fishman'
"""
DECIMAL TO BINARY
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/27/

You are given a decimal (base 10) number, print its binary representation.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing decimal numbers greater or equal to 0,
one per line.

Ignore all empty lines.

For example:

* 2
* 10
* 67

OUTPUT SAMPLE:

Print the binary representation, one per line.

For example:

* 10
* 1010
* 1000011
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        number = int(test_case.strip())
        output = ""
        if number == 0:
            print 0
        else:
            while number > 0:
                next_digit = number % 2
                output += str(next_digit)
                number /= 2
        print output[::-1]
