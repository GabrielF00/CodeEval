__author__ = 'Gabriel Fishman'
"""
LETTERCASE PERCENTAGE RATIO
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/147/

Your task is to write a program which determines (calculates) the percentage ratio of lowercase and uppercase letters.

INPUT SAMPLE:

Your program should accept a file as its first argument. Each line of input contains a string with uppercase and
lowercase letters.

For example:

* thisTHIS
* AAbbCCDDEE
* N
* UkJ

OUTPUT SAMPLE:

For each line of input, print the percentage ratio of uppercase and lowercase letters rounded to the second digit after
the point.

For example:

* lowercase: 50.00 uppercase: 50.00
* lowercase: 20.00 uppercase: 80.00
* lowercase: 0.00 uppercase: 100.00
* lowercase: 33.33 uppercase: 66.67
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.strip()
        num_upper = num_lower = 0
        test_length = len(test)
        for i in range(0, test_length):
            if test[i].islower():
                num_lower += 1
            elif test[i].isupper():
                num_upper += 1
        lower_pct = float(num_lower) / test_length * 100
        upper_pct = float(num_upper) / test_length * 100
        print "lowercase: %.2f" % lower_pct + " uppercase: %.2f" % upper_pct

