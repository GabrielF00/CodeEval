__author__ = 'Gabriel Fishman'
"""
SWAP NUMBERS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/196/

Write a program that, given a sentence where each word has a single digit positive integer as a prefix and suffix, swaps
the numbers while retaining the word in between. Words in the sentence are delimited from each other by a space.

INPUT SAMPLE:

The first argument is a path to a file. Each line of the input file contains one test case represented by a sentence.
Each word in the sentence begins and ends with a single digit positive integer i.e. 0 through 9. Assume all characters
are ASCII.

* 4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
* 5Nobody5 7expects3 5the4 6Spanish4 9inquisition0

OUTPUT SAMPLE:

For each test case, print to standard output the sentence obtained by swapping the numbers surrounding each word, one
per line.

* 0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5
* 5Nobody5 3expects7 4the5 4Spanish6 0inquisition9
"""

import re
import sys

pattern = re.compile("(\d)(\w+)(\d)")
with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        words = test.strip().split(" ")
        swapped_words = []
        for word in words:
            swapped_words.append(re.sub(pattern, r'\3\2\1', word))
        print " ".join(swapped_words)
