#!/bin/python3

import sys
from collections import defaultdict

def cost(B,n):
    d = defaultdict(list)
    d[0]=[0,0]
    for i in range(1,n):
        d[i] = [max(d[i-1][0], d[i-1][1] + (B[i-1]-1)),
                max(d[i-1][0] + (B[i]-1), d[i-1][1] + abs(B[i]-B[i-1])) ]
    return max(d[n-1][0], d[n-1][1])

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        B = list(map(int, input().split()))
        result = cost(B,n)
        print(result)
