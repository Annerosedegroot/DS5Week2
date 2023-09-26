import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_initial_graph(n0:int):
    """Genereer de initial graph.
    
    input
    ---------
    n0: int
    aantal nodes aan startnetwerk
    """
    return nx.star_graph(n0)

def calculate_probabilities(G, alpha):
    """Bereken de kans dat een nieuwe node aan een bestaande node verbind
    
    input
    --------
    G: netwerk
    alpha: betrouwbaarheid/kans
    """
    probabilities = {}

    # Bereken de kans dat een node aan een andere node verbind met kans alpha
    linked_pages = list(G.neighbors(3))
    for page in linked_pages:
        probabilities[page] = alpha / len(linked_pages)

    # Bereken de kans dat een nieuwe node aan een 'unlinked' page verbind met kans 1 - alpha
    unlinked_pages = [node for node in G.nodes() if node != 3 and node not in linked_pages]
    for page in unlinked_pages:
        probabilities[page] = (1 - alpha) / len(unlinked_pages)

    return probabilities

# def random_surfer(G, alpha, T):
#     """Simuleer de websurfer en de PageRank
    
#     input
#     ---------
#     G: netwerk
#     Alpha: betruwbaarheid/kans, float
#     T: clicks?
    
#     Returns: 
#     page_rank
#     """
#     page_rank = {node: 0 for node in G.nodes()}
#     current_page = 3  # Starting from page 3

#     for _ in range(T):
#         probabilities = calculate_probabilities(G, alpha)
#         next_page = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
#         page_rank[next_page] += 1
#         current_page = next_page

#     # Normalize PageRank values
#     for page in page_rank:
#         page_rank[page] /= T

#     return page_rank

# Genereer het netwerk gebaseerd op Barabasi-Albert algoritme
seed_value = 42  # kies een seed (zodat steeds het zelfde netwerk ontstaat)
initial_graph = generate_initial_graph(5)
G = nx.barabasi_albert_graph(400, 4, seed=seed_value, initial_graph=initial_graph)

# simuleer de websurfer en bereken pagerank (of gebaseerd op pagerank)
alpha = 0.85  # alph staat ook niet vast, verplaatsen
T = 100  #deze stata niet vast maar moet gebruikt worden in de andere functie
#page_rank = random_surfer(G, alpha, T)

# Visualize the network
pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=False, node_size=50)

# Add labels to the nodes with just the numbers (1-400)
labels = {node: str(node) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_color='black')
plt.show()

