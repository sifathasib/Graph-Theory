from graph import Graph

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }



graph = Graph(g)

graph.add_edge({"ab", "fg"})
graph.add_edge({"xyz", "bla"})

print("")
print("Vertices of graph:")
print(graph.all_vertices())

print("Edges of graph:")
print(graph.all_edges())





