__author__ = 'Gabriel Fishman'

"""DATA RECOVERY
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/140/

Your friends decided to make fun of you. They have installed a script on your computer which shuffled all words within
a text. It is a joke, so they have left hints for each sentence. The hints will allow you to rebuild the data easily,
but you need to find out how to use them.

Your task is to write a program which reconstructs each sentence out of a set of words and prints out the original
sentences.

INPUT SAMPLE:

Your program should accept a path to a filename as its first argument. Each line is a test case which consists of a set
of words and a sequence of numbers separated by a semicolon. The words within a set and the numbers within a sequence
are separated by a single space.

For example:

2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2
programming first The language;3 2 1
programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9

OUTPUT SAMPLE:

Print out a reconstructed sentence for each test case, one per line.

For example:
However, it was not implemented until 1998 and 2000
The first programming language
The Manchester Mark 1 ran programs written in Autocode from 1952
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        components = test_case.strip().split(";")
        words = components[0].split(" ")
        nums = components[1].split(" ")
        result = ["X" for x in range(0, len(words))]
        nums = [int(x) for x in nums]
        for i in range(0, len(nums)):
            result[int(nums[i] - 1)] = words[i]
        result[result.index("X")] = words[len(nums)]
        print " ".join(result)

