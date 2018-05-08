#!/bin/python3

import sys

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, n1, n2, w):
        self.nodes.add(n1)
        self.nodes.add(n2)
        self.edges.setdefault(n1, {}).update({n2: w})
        self.edges.setdefault(n2, {}).update({n1: w})
        
    def Prims(self,s):
        visited = {s : 0}
        while len(visited) != n:
            lowestCost = (None, float('inf'))
            for node in visited:
                for nextNode,weight in self.edges[node].items():
                    if nextNode not in visited and weight < lowestCost[1]:
                        lowestCost = (nextNode, weight)
            node, weight = lowestCost
            visited[node] = weight
        return sum(visited.values())
        

if __name__ == "__main__":
    graph = Graph()
    n, m = list(map(int,input().split()))
    for _ in range(m):
        edge = list(map(int,input().split()))
        graph.add_edge(edge[0],edge[1],edge[2])
    start = int(input())
    result = graph.Prims(start)
    print(result)