import copy 

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    # checking edge exists
    def get_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] == 1:
            return True
        else: 
            return False
    # Remove edges
    def remove_edge(self, v1, v2):
        #if self.adjMatrix[v1][v2] == 0:
        #    print("No edge between %d and %d" % (v1, v2))
        #    return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(val,end=" "),
            print()


def main():
    V,E = map(int,input().split())
    g = Graph(V+1)
    for i in range(E):
        x,y = map(int,input().split())
        g.add_edge(x, y)

    
    vertex =[x+1 for x in range(V)]
    for i in range(len(vertex)):
        graph = copy.deepcopy(g) 
        edge_count = 0
        l1 = vertex[:i+1]
        l2= vertex[i+1:]
        for j in range(len(l1)):
            for k in l1[i+1:]:
                graph.remove_edge(l1[j],k)
        for j in range(len(l2)):
            for k in l2[i+1:]:
                graph.remove_edge(l2[j],k)
        for i in l1:
            for j in l2:
                if (graph.get_edge(i,j)):
                    edge_count += 1
        if edge_count >= (E/2):
            print(len(l1))
            for i in l1:
                print(i,end=" ")
            print()
            print(len(l2))
            for i in l2:
                print(i,end=" ")
            break 
if __name__ == '__main__':
    main()