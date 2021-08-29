

'''
for i in range(len(vertex)):
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
            if (graph.get_edge(i,j))
                edge_count += 1
    if edge_count >= E:
        print(len(l1)+1)
        for i in l1:
            print(i,end=" ")
        print(len(l2)+1)
        for i in l2:
            print(i.end=" ")
        break 
    print(l1)
    print(l2)
'''

V = 4 

vertex_set =[x+1 for x in range(V) ]
print(vertex_set)
