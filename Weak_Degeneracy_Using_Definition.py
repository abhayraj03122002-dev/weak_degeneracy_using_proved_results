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
# DELSAVE
# -------------------------------
def delsave(G, f, u, w):
    new_G = G.copy()
    new_f = f.copy()
    for v in list(new_G.neighbors(u)):
        if w is not None and v == w and f[u] > f[w]:
            continue
        new_f[v] -= 1
        if new_f[v] < 0:
            return None, None
    new_G.remove_node(u)
    del new_f[u]
    return new_G, new_f
# -------------------------------
# RECURSION
# -------------------------------
def can_delete_all_full(G, f):
    if len(G.nodes) == 0:
        return True
    for u in list(G.nodes):
        for w in list(G.neighbors(u)) + [None]:
            new_G, new_f = delsave(G, f, u, w)
            if new_G is not None:
                if can_delete_all_full(new_G, new_f):
                    return True
    return False
# -------------------------------
# WEAK DEGENERACY
# -------------------------------
def weak_degeneracy(G, start_d, end_d):
    # Step 0: initialize bounds with degeneracy
    bounds = {end_d}
    # Step 1: check from end_d - 1 downward
    for d in range(end_d - 1, start_d - 1, -1):
        # Step 2: assign f(v) = d
        f = {}
        for v in G.nodes:
            f[v] = d
        # Step 3: check deletion
        result = can_delete_all_full(G, f)
        # Step 4: if True then add
        if result == True:
            bounds.add(d)
        else:
            # Step 5: stop immediately on first False
            break
    # Step 6: return minimum valid value
    return min(bounds)
#-------Input-------------------
G = input_graph()
# -------------------------------
# OUTPUT
# -------------------------------
# Step 1: take inputs from user
start_d = int(input("Enter starting value of d: "))
end_d = int(input("Enter degeneracy of graph (upper limit): "))

# Step 2: call function
wd = weak_degeneracy(G, start_d, end_d)

# Step 3: print result
if wd is None:
    print("No valid weak degeneracy found in given range")
else:
    print("\nWeak Degeneracy Number <=", wd)
