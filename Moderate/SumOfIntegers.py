__author__ = 'Gabriel Fishman'
"""
SUM OF INTEGERS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/17/

Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:

The first argument is a path to a filename containing a comma-separated list of integers, one per line.

For example:

* -10,2,3,-2,0,5,-15
* 2,3,-2,-1,10

OUTPUT SAMPLE:

Print to stdout the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the
one with the largest sum, and print that sum.

For example:

* 8
* 12
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    '''
    This approach uses Kadane's Algorithm, which uses dynamic programming to solve in O(n) time.
    This is adapted from: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    '''
    for test_case in test_cases:
        num_arr = [int(x) for x in test_case.strip().split(",")]
        max_ending_here = num_arr[0]
        max_so_far = num_arr[0]
        for x in num_arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        print max_so_far
