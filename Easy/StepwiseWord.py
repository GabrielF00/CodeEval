__author__ = 'Gabriel Fishman'

"""
STEPWISE WORD
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/202/
Print the longest word in a stepwise manner.

INPUT SAMPLE:

The first argument is a path to a file. Each line contains a test case with a list of words that have different or the
same length.

For example:

1. cat dog hello
2. stop football play
3. music is my life

OUTPUT SAMPLE:

Find the longest word in each line and print it in one line in a stepwise manner. Separate each new step with a space.
If there are several words of the same length and they are the longest, then print the first word from the list.


1. h *e **l ***l ****o
2. f *o **o ***t ****b *****a ******l *******l
3. m *u **s ***i ****c
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        words = test_case.strip().split(" ")
        max_length = 0
        longest_word = ""
        for word in words:
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word
        to_print = ""
        for i in range(0, max_length):
            for j in range(0, i):
                to_print += "*"
            to_print += longest_word[i] + " "
        print to_print

