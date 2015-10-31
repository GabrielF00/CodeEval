import math
import sys

__author__ = 'Gabriel Fishman'

"""
Minimum Coins

See: https://www.codeeval.com/open_challenges/74/

You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive at.
Find the minimum number of coins to arrive at it.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive
integer number which represents the total you have to arrive at. E.g.

* 11
* 20

OUTPUT SAMPLE:

Print out the minimum number of coins required to arrive at the total. E.g.

* 3
* 4
"""
denominations = [5, 3, 1]

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        total = int(test.strip())
        num_coins = 0
        for coin in denominations:
            num_current_coin = int(math.floor(total / coin))
            total -= num_current_coin * coin
            num_coins += num_current_coin
        print num_coins
