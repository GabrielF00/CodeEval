import sys

__author__ = 'Gabriel Fishman'
"""
ARRAY ABSURDITY
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenge_scores/?pkbid=41

Imagine we have an immutable array of size N which we know to be filled with integers ranging from 0 to N-2, inclusive.
Suppose we know that the array contains exactly one duplicated entry and that duplicate appears exactly twice. Find the
duplicated entry. (For bonus points, ensure your solution has constant space and time proportional to N)

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Ignore
all empty lines. Each line begins with a positive integer(N) i.e. the size of the array, then a semicolon followed by a
comma separated list of positive numbers ranging from 0 to N-2, inclusive. i.e eg.

* 5;0,1,2,3,0
* 20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14

OUTPUT SAMPLE:

Print out the duplicated entry, each one on a new line eg

* 0
* 4
"""
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        array_size = int(test.split(";")[0])
        input_array = test.strip().split(";")[1].split(',')
        input_array = [int(x) for x in input_array]
        input_sum = sum(input_array)
        # the array has values 0 -> array_size - 2
        max_int = array_size - 2
        # the sum of the values 0 -> N = N(N+1) / 2
        summation = (max_int * (max_int + 1)) / 2
        # if there were no duplicates, the sum of the array would be summation
        # since there is one duplicate, we can find its value by subtracting summation from
        # input_sum
        print input_sum - summation
