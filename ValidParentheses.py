__author__ = 'Gabriel Fishman'

"""
Valid Parentheses:

See: https://www.codeeval.com/open_challenge_scores/?pkbid=68

Given a string comprising just of the characters (,),{,},[,] determine if it is well-formed or not.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line in this file contains a string
comprising of the characters mentioned above. E.g.

* ()
* ([)]

OUTPUT SAMPLE:

Print out True or False if the string is well-formed. E.g.

* True
* False
"""

import sys

test_cases = open(sys.argv[1], 'r')

matching_symbols = {"}": "{", "]": "[", ")": "("}

for test in test_cases:
    chars = list(test)
    stack = []
    valid = True
    for c in chars:
        if c == "{" or c == "[" or c == "(":
            stack.append(c)
        if c == "}" or c == "]" or c == ")":
            if not stack:
                valid = False
                break
            last_char = stack.pop()
            if last_char != matching_symbols[c]:
                valid = False
                break
    if not valid:
        print False
    else:
        if not stack:
            print True
        else:
            print False

test_cases.close()