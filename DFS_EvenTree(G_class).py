#!/bin/python3

import os
import sys
import copy
from collections import defaultdict

class Graph:
    g=defaultdict(set)
    def add_edge(self,pair): 
        self.g[pair[0]].add(pair[1])
        self.g[pair[1]].add(pair[0])
    def remove_edge(self,pair): 
        self.g[pair[0]].remove(pair[1])
        self.g[pair[1]].remove(pair[0])
    def neighbors(self, node):
        return self.g[node]

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph.neighbors(vertex) - visited)
    return len(visited)

if __name__ == '__main__':
    n_nodes, n_edges = map(int, input().split())
    graph = Graph()
    edges = []
    for _ in range(n_edges):
        edge = list(map(int, input().split()))
        edges.append(edge)
        graph.add_edge(edge)
    
    count=0
    for i in range(n_edges):
        cutted_graph=copy.deepcopy(graph)
        cutted_graph.remove_edge(edges[i])
        # because n is even, we test only one part of the cutted tree
        if dfs(cutted_graph,edges[i][0])%2==0:
            count+=1
    
    print(count)