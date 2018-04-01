#!/bin/python3

import sys
from collections import defaultdict

def bfs(n, m, graph, start, w):
    
    distances = dict()
    for i in range(1,n+1) : distances[i]=-1
    distances[start]=0
    
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if distances[neighbor]==-1:
                distances[neighbor]=distances[node]+w
                queue.append(neighbor)
                
    del distances[start]
    return distances.values()
    

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        graph = defaultdict(set)
        for edges_i in range(m):
            edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
            graph[edges_t[0]].add(edges_t[1])
            graph[edges_t[1]].add(edges_t[0])
        s = int(input().strip())
        result = bfs(n, m, graph, s, 6)
        print (" ".join(map(str, result)))