__author__ = 'Gabriel Fishman'

"""
PANGRAMS:

See: https://www.codeeval.com/open_challenges/37/

The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet.
Such sentences are called pangrams. You are to write a program, which takes a sentence, and returns all the letters it
is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence,
and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII
characters.In case the input sentence is already a pangram, print out the string NULL

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. This file will contain several text strings,
one per line. E.g.

A quick brown fox jumps over the lazy dog
A slow yellow fox crawls under the proactive dog

OUTPUT SAMPLE:

Print out all the letters each string is missing in lowercase, alphabetical order . E.g.

NULL
bjkmqz
"""

import copy
import re
import sys

test_cases = open(sys.argv[1], 'r')

alphabet = ["a", "b", "c" , "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

nonalpha_chars = re.compile("[^a-zA-Z]")

for test in test_cases:
    test = test.lower()
    test = re.sub(nonalpha_chars, "", test)
    results = copy.copy(alphabet)
    for c in list(results):
        if test.count(c) > 0:
            results.remove(c)
    if len(results) == 0:
        print "NULL"
    else:
        print "".join(results)

test_cases.close()
