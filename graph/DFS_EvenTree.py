#!/bin/python3

import os
import sys
import copy
from collections import defaultdict

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return len(visited)

if __name__ == '__main__':
    n_nodes, n_edges = map(int, input().split())
    graph = defaultdict(set)
    edges = []
    for _ in range(n_edges):
        edge = list(map(int, input().split()))
        edges.append(edge)
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    
    count=0
    for i in range(n_edges):
        cutted_graph=copy.deepcopy(graph)
        cutted_graph[edges[i][0]].remove(edges[i][1])
        cutted_graph[edges[i][1]].remove(edges[i][0])
        # because n is even, we test only one part of the cutted tree
        if dfs(cutted_graph,edges[i][0])%2==0:
            count+=1
    
    print(count)