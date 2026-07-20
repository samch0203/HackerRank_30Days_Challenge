#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]

    count = 0
    maximum = 0

    for bit in binary:
        if bit == '1':
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    print(maximum)
