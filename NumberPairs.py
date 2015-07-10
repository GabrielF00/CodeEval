__author__ = 'Gabriel Fishman'

"""
NUMBER PAIRS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/34/

You are given a sorted array of positive integers and a number 'X'.
Print out all pairs of numbers whose sum is equal to X.
Print out only unique pairs and the pairs should be in ascending order

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print the string NULL e.g.

* 1,2,3,4,6;5
* 2,4,5,6,9,11,15;20
* 1,2,3,4;50

OUTPUT SAMPLE:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order
i.e the first number of each pair should be in ascending order. E.g.

* 1,4;2,3
* 5,15;9,11
* NULL
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for input in test_cases:
        inputArr = input.split(";", 1)
        arr = inputArr[0]
        arr = arr.split(",")
        arr = [int(x) for x in arr]
        sum = int(inputArr[1].strip())
        pairs = []
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == sum:
                    pairs.append(str(arr[i]) + "," + str(arr[j]))

        if len(pairs) == 0:
            print "NULL"
        else:
            print ";".join(pairs)
