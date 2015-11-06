import itertools
import sys

__author__ = 'Gabriel Fishman'
"""
NUMBER OPERATIONS
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/190/

Alice has invented a new card game to play with Bob. Alice made a deck of cards with random values between 1 and 52.
Bob picks 5 cards. Then, he has to rearrange the cards so that by utilizing the operations plus, minus, or times, the
value of the cards reach Alice's favorite number, 42. More precisely,
find operations such that ((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42.

Help Bob by writing a program to determine whether it is possible to reach 42 given 5 card values.

For example, Bob picks 5 cards out of the deck containing 60, 1, 3, 5, and 20. Bob rearranges the cards and supplies
four operations, so that 5 * 20 - 60 + 3 - 1 = 42.

INPUT SAMPLE:

The input consists of five integers on a line, separated by spaces. Each integer V is 0 <= V <= 52.

* 44 6 1 49 47
* 34 1 49 2 21
* 31 38 27 51 18

OUTPUT SAMPLE:

For each test case print a line containing "YES" if it is possible to reach the value 42 according to the rules of the
game, or "NO" otherwise.

* NO
* YES
* NO
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


ops = [
    add,
    sub,
    mul,
]


def check_input(vals):
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                for op4 in ops:
                    result = op1(vals[0], vals[1])
                    result = op2(result, vals[2])
                    result = op3(result, vals[3])
                    result = op4(result, vals[4])
                    if result == 42:
                        return True
    return False


def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            values = [int(x) for x in list(test.strip().split(" "))]
            can_reach_42 = "NO"
            for permutation in itertools.permutations(values):
                if check_input(permutation):
                    can_reach_42 = "YES"
                    break
            print can_reach_42

if __name__ == "__main__":
    main()
