#!/bin/python3
import sys
from collections import defaultdict


def DFS(graph, start, visited):
    visitedCluster, stack = set(), [start]
    while stack:
        node = stack.pop()
        if visited[node]==False:
            visited[node]=True
            visitedCluster.add(node)
            stack.extend([neighbor for neighbor in graph[node] if visited[neighbor]==False])
    return len(visitedCluster)


def roadsAndLibraries(n, c_lib, c_road, graph):
    if (c_lib<c_road): 
        return n*c_lib
    else:
        global visited
        visited = [False]*(n+1)
        clusterSize = 0
        totalCost = 0
        for node in range(1,n+1):
            if visited[node]==False:
                clusterSize = DFS(graph, node, visited)
                totalCost += c_lib + (clusterSize-1)*c_road
        return totalCost

            
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, c_lib, c_road = list(map(int,input().split()))
        graph = defaultdict(set)
        for _ in range(m):
            edge = list(map(int, input().split()))
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        result = roadsAndLibraries(n, c_lib, c_road, graph)
        print(result)