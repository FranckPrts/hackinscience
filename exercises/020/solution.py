#! /usr/bin/env python

import sys

if len(sys.argv) > 1:

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    r = a - b

    print(r)   
	
else:


    print("usage: python3 solution.py OP1 OP2")