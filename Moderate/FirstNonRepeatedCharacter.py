import sys

__author__ = 'Gabriel Fishman'
"""
FIRST NON-REPEATED CHARACTER
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/12/

Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains strings.

For example:

* yellow
* tooth

OUTPUT SAMPLE:

Print to stdout the first non-repeated character, one per line.

For example:

* y
* h
"""

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        freqs = {}
        for i in range(len(test.strip())):
            if test[i] in freqs:
                freqs[test[i]] += 1
            else:
                freqs[test[i]] = 1
        for i in range(len(test.strip())):
            if freqs[test[i]] == 1:
                print test[i]
                break
