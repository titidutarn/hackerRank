from collections import defaultdict

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited 

""" Store values in data with (weight,count) as key"""
data = defaultdict()
n, m = map(int,input().split())
for _ in range(m):
    edge1, edge2, weight = map(int,input().split())
    count = 0
    key = "%s,%s" % (weight, count)
    while key in data.keys():
        count += 1
        key = "%s,%s" % (weight, count)
    data[key] = edge1,edge2

    
trip = defaultdict(set)
res = 0

for edge in sorted(data,key=lambda x: int(x.split(',')[0])):

    """If [edge][0] not in clique containing [edge][1] and [edge][1] not in clique containing [edge][0]"""
    if (data[edge][0] not in dfs(trip,data[edge][1])) and (data[edge][1] not in dfs(trip,data[edge][0])):

        """If none found...  connect the vertexes"""
        trip[int(data[edge][0])].add(int(data[edge][1]))
        trip[int(data[edge][1])].add(int(data[edge][0]))

        """Add the weight to the answer"""
        res += int(edge.split(',')[0])

print(res)