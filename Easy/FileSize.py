__author__ = 'Gabriel Fishman'
"""
FILE SIZE
CHALLENGE DESCRIPTION:

See: https://www.codeeval.com/open_challenges/26/

Print the size of a file in bytes.

INPUT:

The first argument to your program has the path to the file you need to check the size of.

OUTPUT SAMPLE:

Print the size of the file in bytes. E.g.

* 55
"""

import os.path
import sys

print os.path.getsize(sys.argv[1])
