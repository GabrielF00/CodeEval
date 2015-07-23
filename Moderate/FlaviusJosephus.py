__author__ = 'Gabriel Fishman'
"""
FLAVIUS JOSEPHUS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/75/

Flavius Josephus was a famous Jewish historian of the first century, at the time of the destruction of the Second Temple.
According to legend, during the Jewish-Roman war he was trapped in a cave with a group of soldiers surrounded by Romans.
Preferring death to capture, the Jews decided to form a circle and, proceeding around it, to kill every j'th person
remaining until no one was left. Josephus found the safe spot in the circle and thus stayed alive.

Write a program that returns a list of n people, numbered from 0 to n-1, in the order in which they are executed.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma
separated positive integers n and m, where n is the number of people and every m'th person will be executed. E.g.

* 10,3
* 5,2

OUTPUT SAMPLE:

Print out the list of n people (space delimited) in the order in which they will be executed. E.g.

* 2 5 8 1 6 0 7 4 9 3
* 1 3 0 4 2
"""
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        test_case_arr = test_case.split(",", 1)
        list_size = int(test_case_arr[0])
        steps = int(test_case_arr[1].strip())
        ptr = -1
        arr = [x for x in range(list_size)]
        output = []
        for i in range(0, list_size):
            # Keep moving the pointer until we've hit 'steps' number of array positions that haven't been crossed off
            valid_steps = 0
            while valid_steps < steps:
                ptr = (ptr + 1) % list_size
                if arr[ptr] != 'x':
                    valid_steps += 1
            output.append(str(ptr))
            arr[ptr] = 'x'
        print " ".join(output)
