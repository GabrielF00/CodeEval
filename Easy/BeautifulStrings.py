__author__ = 'Gabriel Fishman'

"""
BEAUTIFUL STRINGS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/83/
Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.

When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on.
So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string
in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The
beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't
care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter.
(Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most
beautiful. What is the maximum possible beauty of this string?

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file has a sentence. E.g.

* ABbCcc
* Good luck in the Facebook Hacker Cup this year!
* Ignore punctuation, please :)
* Sometimes test cases are hard to make up.
* So I just go consult Professor Dalves

OUTPUT SAMPLE:

Print out the maximum beauty for the string. E.g.

* 152
* 754
* 491
* 729
* 646
"""

import re
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        test_case = test_case.strip().lower()
        test_case = re.sub(r'[^a-z]', '', test_case)
        charArr = list(test_case)
        charDict = dict()
        for i in charArr:
            if i in charDict:
                charDict[i] += 1
            else:
                charDict[i] = 1
        sorted_chars = sorted(charDict.values(), reverse=True)
        charValue = 26
        stringValue = 0
        for i in sorted_chars:
            stringValue += charValue * i
            charValue -= 1
        print stringValue
