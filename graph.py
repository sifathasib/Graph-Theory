class Graph(object):
    
    def __init__(self,graph_dict = None):
        '''initailaize a graph object '''
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict
    
    def edges(self,vertice):
        '''returns the all edges of a vertice'''
        return self._graph_dict[vertice]
    
    def all_vertices(self):
        ''' return all vertices of a graph '''
        return set(self._graph_dict.keys())
    def all_edges(self):
        ''' return all edges of agraph'''
        return self.__generate_edges()
    def add_vertex(self,vertex):
        '''add a new vertex for a graph'''
        if vertex not in self._graph_dict:
            self._graph_dict[vertex]=[]
    def add_edge(self,edge):
        '''add edge to a graph, 
        edge can be tuple,set or list'''
        edge = set(edge)
        vartex1,vartex2 = tuple(edge)
        for x,y in [(vartex1,vartex2),(vartex2,vartex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]
            

    def __generate_edges(self):
        '''A static method generating the edges of the graph'''
        edges = []
        for node in self._graph_dict:
            for neigbor in self._graph_dict[node]:
                if {neigbor,node} not in edges:
                    edges.append({node,neigbor})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
        
    