__author__ = 'Gabriel Fishman'
"""
STRING MASK
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/199/

You've got a binary code which has to be buried among words in order to unconsciously pass the cipher.
Create a program that would cover the word with a binary mask. If, while covering, a letter finds itself as 1, you have
to change its register to the upper one, if it's 0, leave it as it is. Words are always in lower case and in the same
row with the binary mask.

INPUT SAMPLE:

The first argument is a path to a file. Each row contains a test case with a word and a binary code separated with
space, inside of it. The length of each word is equal to the length of the binary code.

For example:

* hello 11001
* world 10000
* cba 111

OUTPUT SAMPLE:

Print the encrypted words without binary code.

For example:

* HEllO
* World
* CBA
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        word = test.split(" ")[0]
        binary = test.strip().split(" ")[1]
        result = ""
        for i in range(0, len(binary)):
            if binary[i] == '1':
                result += word[i].upper()
            else:
                result += word[i]
        print result


