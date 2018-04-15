#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = list(map(int,input().split()))
    arr = []
    for arr_i in range(n):
        arr.append([v for v in input().split()])
    k = int(input())
    print('\n'.join(map(' '.join,sorted(arr, key=lambda x:int(x[k])))))