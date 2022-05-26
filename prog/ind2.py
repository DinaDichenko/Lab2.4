#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(float, input("Enter a list items:").split()))
    min_A = 10**6
    count = 0

    for i, item in enumerate(A):
        if item < 0:
            count += 1
    if count < 2:
        print("Not enough negative elements", file=sys.stderr)
        exit(1)
    count = 0

    for i, item in enumerate(A):
        if item < min_A:
            min_A = item
        if item < 0 and count < 1:
            count += 1
            gr1 = i
    count = 0

    for i, item in enumerate(A):
        if item < 0 and count < 2:
            count += 1
            gr2 = i

    s = 0
    for j in range(gr1 + 1, gr2):
        s += A[j]
    print(
        "The number of the minimum list item:", min_A, "\nSum =", s, "\nSorted list:", sorted(A, key=abs)
          )
