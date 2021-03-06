#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input("Enter a list of 10 items:").split()))
    s = 1
    count = 0

    if len(A) != 10:
        print("Invalid list size", file=sys.stderr)
        exit(1)

    for i, item in enumerate(A):
        if item < 0:
            s *= item
            count += 1
    if count == 0:
        s = 0
    print("The product of negative elements", s)
