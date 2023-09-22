import networkx as nx
import random
import matplotlib.pyplot as plt

#niet schrikken dat het netwerk maar 10 nodes heeft, kun je aanpassen in regel 26 maar doe maar pas als alles werkt

def genereer_barabasi(n0, n, M):
    """Genereert een netwerk gebaseerd op het barabasi-albert algoritme
    Input:
    ----------
    no: int
        startaantal nodes aan start_graph
    n: int
        Aantal gewenste totale nodes
    M: int
        aantal edges vanuit iedere nieuwe node
    
    Return
    -----------
    G: graph (ontstane barabasi netwerk)
    """
    # Maak een ster netwerk met starthoeveelheid nodes n0
    G = nx.star_graph(n0)

    # Voeg de resterende nodes een voor een toe
    for i in range(n0 + 1, n+1): ############ naar n+1 want is meteen generiek, 
                                #maar dit is overzichtelijker voor wat er gebeurd. Check ook de probability dit is raar
                                #node 0 zou toch de kleinste kans moeten hebben om verbonden te geraken met node 6, die lijst zou omgekeer dmoeten zijn???
        # Voeg de nieuwe node toe
        G.add_node(i)

        # Lijst van alle bestaande nodes
        existing_nodes = list(G.nodes)
        #existing_nodes.remove(0)
        
        # Bereken de kansverdeling (page rank?) voor het verbinden van de nieuwe node met bestaande nodes
        node_degrees = dict(G.degree())
        prob = [node_degrees[node] / sum(node_degrees.values()) for node in existing_nodes]
        print(i, prob)
        # Verbind de nieuwe node met M bestaande nodes op basis van de kansverdeling
        selected_nodes = random.choices(existing_nodes, weights=prob, k=M)

        # Voeg edges toe zonder zelfverbindingen
        selected_nodes = [node for node in selected_nodes if node != i]

        for node in selected_nodes:
            G.add_edge(i, node)
    
    return G

def plot_network(G):
    # Genereer de layout met spring_layout
    pos = nx.spring_layout(G)

    # Teken het netwerk
    nx.draw(G, pos, with_labels=True, node_size=50)
    plt.show()

# Aantal initiële nodes in de ster
n0 = 5

# Het gewenste totale aantal nodes in het netwerk
n = 10   # Veranderd naar 10 maar moet 400 zijn.

# Aantal nodes waarmee elke nieuwe node zich verbindt
M = 4

# Creëer het netwerk
G = genereer_barabasi(n0, n, M)

# Teken het netwerk
plot_network(G)
