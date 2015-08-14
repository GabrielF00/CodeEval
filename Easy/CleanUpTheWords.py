__author__ = 'Gabriel Fishman'
"""
CLEAN UP THE WORDS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/205/

You have a list of words. Letters of these words are mixed with extra symbols, so it is hard to define the beginning and
end of each word. Write a program that will clean up the words from extra numbers and symbols.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with a list of words: letters are both lowercase
and uppercase, and are mixed with extra symbols.

For example:

* (--9Hello----World...--)
* Can 0$9 ---you~
* 13What213are;11you-123+138doing7

OUTPUT SAMPLE:

Print the cleaned up words separated by spaces in lowercase letters.

For example:

* hello world
* can you
* what are you doing
"""

import re
import sys

pattern = re.compile('[^a-zA-Z]+')

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip().lower()
        print re.sub(pattern, " ", test).strip()

