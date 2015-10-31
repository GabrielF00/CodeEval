import math
import sys

__author__ = 'Gabriel Fishman'

"""
Cash Register:

See: https://www.codeeval.com/open_challenges/54/

The goal of this challenge is to design a cash register program. You will be given two float numbers.
The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer.
Your register currently has the following bills/coins within it:

'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00

The aim of the program is to calculate the change that has to be returned to the customer.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line
is one test case. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price
(PP) and the second is the cash(CH) given by the customer. eg.

* 15.94;16.00
* 17;16
* 35;35
* 45;50

OUTPUT SAMPLE:

For each set of input produce a single line of output which is the change to be returned to the customer. In case the
CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned,
in terms of the currency values provided. The output should be sorted in highest-to-lowest order (DIME,NICKEL,PENNY).
eg.

* NICKEL,PENNY
* ERROR
* ZERO
* FIVE
"""

denominations = {
     int(100.00 * 100): 'ONE HUNDRED',
     int(50.00 * 100): 'FIFTY',
     int(20.00 * 100): 'TWENTY',
     int(10.00 * 100): 'TEN',
     int(5.00 * 100): 'FIVE',
     int(2.00 * 100): 'TWO',
     int(1.00 * 100): 'ONE',
     int(0.50 * 100): 'HALF DOLLAR',
     int(0.25 * 100): 'QUARTER',
     int(0.10 * 100): 'DIME',
     int(0.05 * 100): 'NICKEL',
     int(0.01 * 100): 'PENNY'
}

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        price = int(float(test.split(";")[0]) * 100)
        cash = int(float(test.strip().split(";")[1]) * 100)
        if cash < price:
            print "ERROR"
        elif cash == price:
            print "ZERO"
        else:
            change = cash - price
            result = []
            for k in sorted(denominations.iterkeys(), reverse=True):
                if k <= change:
                    for i in range(int(math.floor(change / k))):
                        change -= k
                        result.append(denominations[k])
            print ",".join(result)
