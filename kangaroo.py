#!/bin/python3
import sys

def kangaroo(x1, v1, x2, v2):
    if v2>=v1 and x1!=x2:return('NO')
    if (x2-x1)%(v1-v2)!=0:return ('NO')
    return('YES')

x1, v1, x2, v2 = list(map(int,input().split()))
result = kangaroo(x1, v1, x2, v2)
print(result)
