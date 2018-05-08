from collections import Counter

inp = list(map(int,input().split(',')))
C = Counter(inp)
print(sorted(C, key=C.get)[0])
