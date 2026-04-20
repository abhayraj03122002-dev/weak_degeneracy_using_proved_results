import networkx as nx
# -------------------------------
# INPUT GRAPH
# -------------------------------
def input_graph():
    G = nx.Graph()
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of edges: "))
    G.add_nodes_from(range(n))
    print("Enter edges (u v):")
    for _ in range(m):
        u, v = map(int, input().split())
        G.add_edge(u, v)
    return G
# -------------------------------
# DEGENERACY FUNCTION
# -------------------------------
def degeneracy(G):
    G_copy = G.copy()   # work on copy
    max_min_degree = 0  # store answer
    while len(G_copy.nodes) > 0:
        # find node with minimum degree
        min_degree = float('inf')
        min_node = None
        for node in G_copy.nodes:
            deg = G_copy.degree(node)
            if deg < min_degree:
                min_degree = deg
                min_node = node
        # update answer
        if min_degree > max_min_degree:
            max_min_degree = min_degree
        # remove that node
        G_copy.remove_node(min_node)
    return max_min_degree
#-------Input-------------------
G = input_graph()
d = degeneracy(G)
print("\nDegeneracy of graph <=", d)
