import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph):
    G = nx.Graph()

    
    for node in graph.nodes():
        G.add_node(node)


    for node, neighbors in graph.adjacency_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=15)
    plt.show()