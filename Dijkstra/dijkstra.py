from math import inf 

class Graph(object):
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]
        
    def addEdge(self,u,v,w):
        pass

    def minDist(slef,Q,dist):
        minimum = inf 
        min_idx = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in Q:
                minimum = dist[i]
                min_idx = i
        return min_idx
    
    def dijkstra(self,source):
        Q =[]
        dist = [inf] * self.v
        prev =[-1] * self.v
        for vertex in range(self.v):
            Q.append(vertex)
        dist[source] = 0
        while Q:
            u = minDist(self,Q,dist)
            Q.remove(u)
            for v in range(len(self.graph[0])):
                if self.graph[u][v] and v in Q:
                    alt = dist[u]+self.graph[u][v]
                    if alt < dist[v]:
                        dist[v] = alt 
                        prev[v] = u
        return dist,prev            
        
    