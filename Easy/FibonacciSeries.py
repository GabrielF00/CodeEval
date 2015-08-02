__author__ = 'Gabriel Fishman'
"""
FIBONACCI SERIES
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/22/

The fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n >= 1. Given an integer n >= 0,
print out F(n).

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

* 5
* 12

OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

* 5
* 144
"""
import sys


def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        n = int(test_case.strip())
        print fibonacci(n)
