#!/bin/python3
import sys

def getWays(N, coins):
    change=[0]*(N+1)
    change[0]=1
    for c in coins:
        for j in range(c,N+1):
            change[j] += change[j-c]
    return change[N]

n, m = list(map(int,input().split()))
c = list(map(int, input().split()))
print(getWays(n, c))
