from lab10 import *

def vc_approx1(G):
    cover = []
    G_copy = G.copy()

    while(not is_vertex_cover(G, cover)):
        node = random.choice(list(G_copy.adj.keys()))
        G_copy.adj.pop(node)
        cover.append(node)

    return cover


def vc_approx2(G):
    cover = []
    unconnected_vertices = []
    single_edge_vertices = []
    sev_connected_nodes = []
    vertices_to_remove = []

    G_copy = G.copy()
    
    for node in G_copy.adj.keys():
        if(len(G_copy.adj[node]) == 0):
            unconnected_vertices.append(node)
        if(len(G_copy.adj[node]) == 1):
            if(len(G_copy.adj[G_copy.adj[node][0]]) == 1):
                cover.append(node)
                G_copy.adj.pop(G_copy.adj[node][0])
            single_edge_vertices.append(node)
            sev_connected_nodes.append(G_copy.adj[node][0])
    
    cover = cover + remove_recurring_vertices(sev_connected_nodes)

    while(not is_vertex_cover(G, cover)):
        node = random.choice(list(G_copy.adj.keys()))
        G_copy.adj.pop(node)
        cover.append(node)

    return cover
#takes the vertices that are connected to a single vertex, and returns the vertex they're connected to without repeating the same one

def remove_recurring_vertices(list_of_nodes): #some code used from https://stackoverflow.com/questions/4446380/python-check-the-occurrences-in-a-list-against-a-value/4447785#4447785
    vertices = []

    for node in list_of_nodes:
        vertices.append(node)
        found=[]
        for index, suspect in enumerate(list_of_nodes):
            if(node == suspect):
                found.append(index)
        if(len(found) == 1):
            continue
        for i in range(len(found) - 1, 0, -1):
            list_of_nodes.pop(i)
    
    return vertices



G = Graph()
for i in range(1,12):
    G.add_node(i)
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(4,3)
G.add_edge(3,5)
G.add_edge(5,6)
G.add_edge(5,7)
G.add_edge(5,8)
G.add_edge(5,9)
G.add_edge(10,11)
G.add_edge(10,11)
cover1 = [1,3,5]
print(is_vertex_cover(G, cover1))
print(G.adj.keys())
print(vc_approx2(G))
