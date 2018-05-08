#!/bin/python3

import sys
from collections import defaultdict

class Graph(object):
  
    def __init__(self):
        self.g=defaultdict(set)

    def add_edge(self,*args):
        self.g[args[0]].add(args[1])
        self.g[args[1]].add(args[0])

    def neighbors(self, node):
        return self.g[node]

    def dfs(self, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.neighbors(vertex) - visited)
        return visited

    def connected_components(self,n):
        l = list(range(n))
        arr_len = []
        while len(l)>0:
            DFS = self.dfs(l[0])
            arr_len.append(len(DFS))
            l = [v for v in l if v not in DFS]
        return arr_len

def journeyToMoon(n, g):
    countrySizes = g.connected_components(n)
    s = 0
    result = 0
    for size in countrySizes:
        result += s*size
        s += size
    return result

if __name__ == "__main__":
    n, p = list(map(int,input().split()))
    graph = Graph()
    for astronaut_i in range(p):
        edge = list(map(int,input().split()))
        graph.add_edge(edge[0],edge[1])
    result = journeyToMoon(n, graph)
    print(result)