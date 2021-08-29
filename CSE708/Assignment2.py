import sys 
from collections import defaultdict 

graph =defaultdict(list)

V,E = map(int,input().split())
for i in range(E):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


vertex_set = list(graph.keys())
print(vertex_set[1:])
