import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

while True:
    try :
        v = int(input())
        print(fib(v))
    except :
        break
