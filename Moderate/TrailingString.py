__author__ = 'Gabriel Fishman'
"""
TRAILING STRING

See: https://www.codeeval.com/open_challenges/32/
CHALLENGE DESCRIPTION:

There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two comma-delimited strings, one per line.
Ignore all empty lines in the input file.

For example:

* Hello World,World
* Hello CodeEval,CodeEval
* San Francisco,San Jose

OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:

* 1
* 1
* 0
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for input in test_cases:
        if len(input) == 0:
            continue
        inputArr = input.split(",", 1)
        stringA = inputArr[0]
        stringB = inputArr[1].strip()
        if stringA[-len(stringB):] == stringB:
            print 1
        else:
            print 0
