__author__ = 'Gabriel Fishman'
"""
MAX RANGE SUM
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/186/

Bob is developing a new strategy to get rich in the stock market. He wishes to invest his portfolio for 1 or more days,
then sell it at the right time to maximize his earnings. Bob has painstakingly tracked how much his portfolio would have
gained or lost for each of the last N days. Now he has hired you to figure out what would have been the largest total
gain his portfolio could have achieved.

For example:

Bob kept track of the last 10 days in the stock market. On each day, the gains/losses are as follows:

7 -3 -10 4 2 8 -2 4 -5 -2
If Bob entered the stock market on day 4 and exited on day 8 (5 days in total), his gains would have been

16 (4 + 2 + 8 + -2 + 4)
INPUT SAMPLE:

The input contains N, the number of days (0 < N < 10000), followed by N (separated by symbol ";") integers D
(-10000 < D < 10000) indicating the gain or loss on that day.

For example:

* 5;7 -3 -10 4 2 8 -2 4 -5 -2
* 6;-4 3 -10 5 3 -7 -3 7 -6 3
* 3;-7 0 -45 34 -24 7

OUTPUT SAMPLE:

Print out the maximum possible gain over the period. If no gain is possible, print 0.

For example:

* 16
* 0
* 17
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        line = test_case
        params = test_case.strip().split(";", 2)
        num_days = int(params[0])
        daily_results = [int(x) for x in params[1].split(" ")]
        max_sum = 0
        for range_start in range(len(daily_results) - num_days + 1):
            range_sum = sum(daily_results[range_start:range_start+num_days])
            if range_sum > max_sum:
                max_sum = range_sum
        print max_sum


