__author__ = 'Gabriel Fishman'
"""
COMPRESSED SEQUENCE
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/128/

Assume that someone dictates you a sequence of numbers, and you need to write it down. For brevity, he dictates it as
follows: first he dictates the number of consecutive identical numbers, and then - the number itself.

For example:
The sequence below

1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2

is dictated as follows:

two times one, three times three, four times two, three times fourteen, three times eleven, one time two
and you have to write down the sequence

2 1 3 3 4 2 3 14 3 11 1 2

Your task is to write a program that compresses a given sequence using this approach.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument that contains T number of lines. Each line is a test
case represented by a sequence of integers with the length L, where each integer is N separated by a space.


* 40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86
* 86 86 86 86 86 86 86
* 73 73 73 73 41 41 41 41 41 41 41 41 41 41
* 1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2
* 7

OUTPUT SAMPLE:

For each test case, print out a compressed sequence of numbers separated by a single space, one per line.

For example:

* 4 40 8 29 2 57 5 92 10 86
* 4 73 10 41
* 2 1 3 3 4 2 3 14 3 11 1 2
* 1 7
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        nums = test_case.strip().split(" ")
        result = list()
        last_num = nums[0]
        last_num_count = 1
        for i in nums[1:]:
            if i == last_num:
                last_num_count += 1
            else:
                result.append(str(last_num_count))
                result.append(last_num)
                last_num_count = 1
                last_num = i
        result.append(str(last_num_count))
        result.append(last_num)
        print " ".join(result)

