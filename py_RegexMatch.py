import re
p = re.compile('[+-]?\d*\.\d*$')

for _ in range(int(input())):
    m = p.match(input())
    if m: print('True')
    else: print('False')