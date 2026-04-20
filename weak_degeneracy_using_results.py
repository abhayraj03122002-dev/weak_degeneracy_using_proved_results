import math
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
# COMPLETE GRAPH CHECK
# -------------------------------
def is_complete_graph(G):
    n = len(G.nodes)
    return G.number_of_edges() == n * (n - 1) // 2
# -------------------------------
# COMPLETE BIPARTITE CHECK
# -------------------------------
def is_complete_bipartite_graph(G):

    if not nx.is_bipartite(G):
        return False, None, None

    X, Y = nx.bipartite.sets(G)
    m, n = len(X), len(Y)

    if G.number_of_edges() == m * n:
        return True, m, n

    return False, None, None
# ----------------------------------
# ICOSAHEDRAL CHECK
# ----------------------------------
def is_icosahedral_graph(G):
    if len(G.nodes) == 12 and len(G.edges) == 30:
        degrees = [d for _, d in G.degree()]
        return all(d == 5 for d in degrees)
    return False


# -------------------------------
# CYCLE DETECTION (GENERAL k)
# -------------------------------
def has_cycle_length_k(G, k):

    def dfs(start, current, depth, visited):

        if depth == k:
            return start in G.neighbors(current)

        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)

                if dfs(start, neighbor, depth + 1, visited):
                    return True

                visited.remove(neighbor)

        return False

    for node in G.nodes:
        if dfs(node, node, 1, {node}):
            return True

    return False
    
# -------------------------------
# ALL CYCLE LENGTHS
# -------------------------------
def all_cycle_lengths(G):

    n = len(G.nodes)
    cycles = set()

    for k in range(3, n + 1):
        if has_cycle_length_k(G, k):
            cycles.add(k)

    return cycles
    
# -------------------------------
# FORBIDDEN SET CHECK
# -------------------------------
def satisfies_forbidden_set(G, forbidden):

    # Step 1: find all cycle lengths in graph
    cycles = all_cycle_lengths(G)

    # Step 2: check each forbidden cycle
    for k in forbidden:

        # if forbidden cycle is present in graph
        if k in cycles:
            return False   # not allowed

    # Step 3: no forbidden cycle found
    return True

# -------------------------------
# WEAK DEGENERACY
# -------------------------------
def weak_degeneracy(G):

    # TREE
    if nx.is_tree(G):
        return 1

    # COMPLETE GRAPH
    if is_complete_graph(G):
        return len(G.nodes) - 1

    bounds = []

    # COMPLETE BIPARTITE
    is_cb, m, n = is_complete_bipartite_graph(G)
    if is_cb:
        bounds.append(min(m, n))

    # ICOSAHEDRAL
    if is_icosahedral_graph(G):
        bounds.append(4)

    # PLANAR
    is_planar, _ = nx.check_planarity(G)

    if is_planar:

        # GIRTH THEOREM
        g = nx.girth(G)
        if g is not None and g >= 5:
            bounds.append(2)

        # FORBIDDEN SET THEOREMS
        if satisfies_forbidden_set(G, [4, 5, 7, 10]):
            bounds.append(2)

        if satisfies_forbidden_set(G, [4, 5, 7, 11]):
            bounds.append(2)

        if satisfies_forbidden_set(G, [4, 5, 8, 10]):
            bounds.append(2)

        if satisfies_forbidden_set(G, [4, 5, 8, 11]):
            bounds.append(2)

        if satisfies_forbidden_set(G, [4, 6, 8, 10]):
            bounds.append(2)

        if satisfies_forbidden_set(G, [4, 6, 9, 10]):
            bounds.append(2)

        bounds.append(4)

    # BROOKS
    if nx.is_connected(G):

        degrees = [d for _, d in G.degree()]
        d_max = max(degrees)

        if d_max >= 3:
            bounds.append(d_max - 1)

    # USE BEST BOUND
    if bounds:
       return min(bounds)

    else:
       return None

#-------Input-------------------
G = input_graph()

# -------------------------------
# COMPUTATION
# ------------------------------
wd = weak_degeneracy(G)

if wd is None:
    print("Not classified")
else:
    print("weak degeneracy =", wd)
