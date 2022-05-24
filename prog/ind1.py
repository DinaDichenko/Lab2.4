#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    A = list(map(int, input("Enter a list of 10 items:").split()))
    s = 1

    if len(A) != 10:
        print("Invalid list size", file=sys.stderr)
        exit(1)

    for i in range(0, len(A)):
        if A[i] < 0:
            s *= A[i]
    print("The product of negative elements", s)
