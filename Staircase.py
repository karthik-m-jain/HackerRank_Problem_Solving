# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:54:08 2020

@author: Karthik Jain
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        l=[" "]*n
        for j in range(i):
            l[n-j-1]="#"
        for j in range(n):
            print(l[j],end="")
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)

