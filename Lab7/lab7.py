from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len(self)

ex = Graph(7)
print(ex.adj)
ex.add_edge(0, 1)
print(ex.adj)
ex.add_edge(1, 2)
ex.add_edge(1, 3)
ex.add_edge(2, 4)
ex.add_edge(4, 3)
ex.add_edge(4, 5)
ex.add_edge(6, 2)
print(ex.adj)


#q = deque([0])
#print(q)
#q.popleft()
#print(q)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#print(BFS(ex, 0 , 6))

def BFS2(G, node1, node2):
    if not BFS(G, node1, node2):
        return []
    if BFS(G, node1, node2) and node1 == node2: 
        return [node1]
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    path = []
    for node in G.adj:
        if node == node1:
            path.append(node)
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                path.append(node)
                #print(path)
                return path
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                if node not in path:
                    path.append(node)
            #print(Q)
            #print(marked)
    #return False

print(BFS2(ex, 0, 6)) 
#print(BFS2(ex, 0, 9))
#print(BFS2(ex, 0, 0))

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

def DFS2(G, node1, node2):
    if not DFS(G, node1, node2): 
        return []
    if DFS(G, node1, node2) and node1 == node2: 
        return [node1]

    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    path = []
    while len(S) != 0:
        current_node = S.pop()
        if current_node not in path: 
            path.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    path.append(node)
                    print(path)
                    return path
                S.append(node)
            #print(S)
            #print(marked)
    return False

#print(DFS(ex, 0, 0))
#DFS2(ex, 0, 6)

