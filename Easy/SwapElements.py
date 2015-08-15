__author__ = 'Gabriel Fishman'
"""
SWAP ELEMENTS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/112/

You are given a list of numbers which is supplemented with positions that have to be swapped.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

* 1 2 3 4 5 6 7 8 9 : 0-8
* 1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above (2nd line) first you process 0-1, then 1-3.

OUTPUT SAMPLE:

Print the lists in the following way.

* 9 2 3 4 5 6 7 8 1
* 2 4 3 1 5 6 7 8 9 10
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        params = test.strip().split(":")
        input_arr = params[0].strip().split(" ")
        input_arr = [int(x) for x in input_arr]
        swap_commands = params[1].strip().split(",")
        for swap_command in swap_commands:
            start = int(swap_command.split("-")[0])
            end = int(swap_command.split("-")[1])
            temp = input_arr[start]
            input_arr[start] = input_arr[end]
            input_arr[end] = temp
        print " ".join(str(x) for x in input_arr)
