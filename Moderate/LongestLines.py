__author__ = 'Gabriel Fishman'

"""
LONGEST LINES
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/2/
Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based
on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line
indicates the number of lines you should output, the other lines are of different length and are presented randomly.
You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

* 2
* Hello World
* CodeEval
* Quick Fox
* A
* San Francisco

OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:

* San Francisco
* Hello World

"""
""" This implementation 0:00:00.119164 """
from datetime import datetime
import sys

starttime = datetime.now()

with open(sys.argv[1], 'r') as test_cases:
    num_to_print = int(test_cases.readline())
    lines = test_cases.readlines()
    lines = sorted(lines, key=lambda line: len(line), reverse=True)
    for i in range(0, num_to_print):
        print lines[i].strip()

print datetime.now() - starttime