import random
import networkx as nx
import matplotlib.pyplot as plt

# Define parameters
n0 = 5  # Initial number of nodes
N = 400  # Total number of nodes
M = 4   # Number of links new page creates

# Create initial star network
G = nx.star_graph(n0)

#existing_nodes = G.nodes() #[0 1 2 3 4 5]
#G.add_node('nieuw')
#G.add_edge(2, 'nieuw')


edges = []
for i in range(1, N+1):
    G.add_node(i)
    
    # anders zijn er nog geen nodes om aan elkaar te linken
    if i > 1:
        random_existing_node = random.choice(range(1, i))
        edges.append((i, random_existing_node))
    
    # Voeg de edge toe tussen de nieuwe node en de bestaande node
        G.add_edge(i, random_existing_node)
    

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True, node_size = 500)
plt.show()