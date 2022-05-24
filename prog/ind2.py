#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = list(map(float, input("Enter a list items:").split()))
    min_A = 10**6
    count = 0

    for i in range(0, len(A)):
        if A[i] < min_A:
            min_A = A[i]
        if A[i] < 0 and count < 1:
            count += 1
            gr1 = i
    count = 0

    for i in range(0, len(A)):
        if A[i] < 0 and count < 2:
            count += 1
            gr2 = i

    s = 0
    for j in range(gr1 + 1, gr2):
        s += A[j]
    print(
        "The number of the minimum list item:", min_A, "\nSum =", s, "\nSorted list:", sorted(A, key=abs)
          )

