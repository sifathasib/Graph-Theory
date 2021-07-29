from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,vartex,visited):
        visited.add(vartex)
        print(vartex,end=" ")
        for neighbor in self.graph[vartex]:
            if neighbor not in visited:
                self.DFSUtil(neighbor,visited)
    def DFS(self):
        visited = set()
        for vartex in list(self.graph):
            if vartex not in visited:
                self.DFSUtil(vartex,visited)


def main():
    g=Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)
    g.DFS()

if __name__ =='__main__':
    main()