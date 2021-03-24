from lab8 import *
import sys

def prim1(G):
    mst = WeightedGraph(G.number_of_nodes())
    A = [G.number_of_nodes() // 2]
    min_node = 0
    min_edge = (min_node, sys.maxsize)

    while(len(A) != G.number_of_nodes()):
        min_edge = (min_node, sys.maxsize)
        for node in G.adj:
            for edge in G.adj[node]:
                if(edge in mst.adj):
                    continue
                if(node in A and edge[0] in A):
                    continue
                if(node not in A and edge[0] not in A):
                    continue
                if(edge[1] < min_edge[1]):
                    print(min_node, min_edge)
                    min_node = node
                    min_edge = edge

        if(min_node in A):
            A.append(min_edge[0])
            mst.add_edge(min_node, min_edge[0], min_edge[1])
        else:
            A.append(min_node)
            mst.add_edge(min_node, min_edge[0], min_edge[1])

    return mst

def prim2(G):
    mst = WeightedGraph(G.number_of_nodes())

    for node in G.adj:
            mst.add_edge(node, G.adj[node][0][0], G.adj[node][0][1])

    return mst

'''
G = WeightedGraph(8)
G.add_edge(0,7,1)
G.add_edge(2,3,2)
G.add_edge(1,7,3)
G.add_edge(0,2,4)
G.add_edge(5,7,5)
G.add_edge(1,3,6)
G.add_edge(1,5,7)
G.add_edge(2,7,8)
G.add_edge(4,5,9)
G.add_edge(1,2,10)
G.add_edge(4,7,11)
G.add_edge(0,4,12)
G.add_edge(6,2,13)
G.add_edge(3,6,14)
G.add_edge(6,0,15)
G.add_edge(6,4,16)

print(G.adj)
print(sys.maxsize + 1)
print(prim1(G).adj)

print(prim2(G).adj)

'''