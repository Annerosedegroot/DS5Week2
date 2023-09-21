import random
import networkx as nx

# Define parameters
n0 = 5  # Initial number of nodes
N = 400  # Total number of nodes
M = 4   # Number of links new page creates

# Create initial star network
G = nx.star_graph(n0)

# Define a function for preferential attachment
def preferential_attachment(G, M):
    total_degree = sum(dict(G.degree()).values())
    probabilities = [degree / total_degree for node, degree in G.degree()]
    targets = random.choices(list(G.nodes()), probabilities, k=M)
    return targets
print(preferential_attachment(G, M))

# Add nodes and links based on Barabasi-Albert algorithm
#def add_nodes_links(n0, N, targets)
#for i in range(n0, N):
#    targets = preferential_attachment(G, M)
#    G.add_node(i)
#    for target in targets:
#        if target != i:
#            G.add_edge(i, target)
            


